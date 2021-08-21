from flask import Flask, request, Response, jsonify
# import requests , json
from handlers import *
import psutil


# creating an instance of the flask app
app = Flask(__name__)

# route to  get consul cluster status:
@app.route('/v1/api/consulCluster/status', methods=['GET'])
def get_consul_cluster_status():
    '''Function to get status of the cluster'''
    # {"status": 0|1, "message": "<message>"}
    res = respon()
    res.request_handler('health/node/consul-server')
    stat = res.status
    msg = "Consul server is running" if stat == 1 else res.message
    return jsonify(
        status= stat,
        message= msg
    )
    
# route to  get consul summary
@app.route('/v1/api/consulCluster/summary', methods=['GET'])
def get_consul_cluster_summary():
    summ = summary()
    #No. of Registered nodes / Registerd Services
    #  = respon()
    summ.request_handler('agent/metrics')
    p_nodes =  summ.payload['Gauges'] if summ.status == 1 and  summ.payload else 0
    for node in p_nodes:
        if node['Name'] == 'consul.consul.state.nodes':
            summ.registered_nodes = node['Value']
        if node['Name'] == 'consul.consul.state.services':
            summ.registered_nodes = node['Value']

    #Cluster Leader IP and port
    summ.request_handler('status/leader')
    summ.leader = summ.payload if summ.status == 1 else 0

    #Cluster Internal (Raft) Protocol Version
    summ.request_handler('operator/raft/configuration')
    p_protocol =summ.payload['Servers'] if summ.status == 1 and summ.payload['Servers'] else 0
    for x in p_protocol:
            if x['Leader'] == True:
                summ.cluster_protocol = x['ProtocolVersion']
                break
    return jsonify(summ.serialize())


# Route to get Cluster Members (Registered Nodes)
@app.route('/v1/api/consulCluster/members', methods=['GET'])
def get_consul_cluster_members():
    node_list = []
    res =respon()
    res.request_handler('/catalog/nodes')
    nodes = res.payload
    if res.status and nodes:
        for node in nodes:
            node_list.append(node['Node'])
    return jsonify(status = res.status, messgae = res.message, registered_nodes = node_list)

# Route to Docker system info
@app.route('/v1/api/consulCluster/systemInfo', methods=['GET'])
# {"vCpus": <>, "MemoryGB": <>, <metric3>: <>}0
def get_consul_cluster_systemInfo():
    return jsonify(
        vCpus = psutil.cpu_count(),
        CpuLoadAvaragePercent = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()], # Return the average system load over the last 1, 5 and 15 minutes as a tuple
        vMemoryTotalGB =psutil.virtual_memory().total / (3*1024.0) ,
        vMemoryUsedMB = psutil.virtual_memory().used / (2*1024.0),
        vMemoryAvailablePrecent = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,
        swapMemoryUsedMB = psutil.swap_memory().used / (2*1024.0),
        DiskUsageTotalGB  = psutil.disk_usage('/').total / (3*1024.0),
        DiskUsagePercent = psutil.disk_usage('/').percent,
        NetworkIOCountersBytesSent = psutil.net_io_counters().bytes_sent / 1024.0,
        NetworkIOCountersBytesReceived = psutil.net_io_counters().bytes_recv / 1024.0,
        )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
