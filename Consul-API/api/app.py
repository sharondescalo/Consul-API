from flask import Flask, request, Response, jsonify
import requests
from requests.exceptions import HTTPError

# creating an instance of the flask app
app = Flask(__name__)

# route to  get consul cluster status:
@app.route('/v1/api/consulCluster/status', methods=['GET'])
def get_consul_cluster_status():
    '''Function to get status of the cluster'''
    # {"status": 0|1, "message": "<message>"}
    stat = 0 
    msg = 0
    url = ' http://127.0.0.1:8500/v1/health/node/consul-server'
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as http_err:
        msg = format(f'HTTP error occurred: {http_err}')
        stat = 0
    except Exception as err:
        msg = print(f'Other error occurred: {err}')
        stat = 0
    else:
            # payload=r.json()
            # if payload[0]['Status'] == "passing" and payload[0]['Output'] == "Agent alive and reachable":
                stat = 1
                msg = "Consul server is running"
    return jsonify(
        status= stat,
        message= msg
    )

# route to  get consul summary
@app.route('/v1/api/consulCluster/summary', methods=['GET'])
def get_consul_cluster_summary():
    return jsonify(
        registered_nodes = {},
        registered_services = {},
        leader = {},
        cluster_protocol = {}
        )

# route to get cluster members
@app.route('/v1/api/consulCluster/members', methods=['GET'])
def get_consul_cluster_members():
    return jsonify(registered_nodes = [])

# route to Docker system info
@app.route('/v1/api/consulCluster/systemInfo', methods=['GET'])
# {"vCpus": <>, "MemoryGB": <>, <metric3>: <>}
def get_consul_cluster_systemInfo():
    return_value = {}
    return jsonify(return_value)

if __name__ == "__main__":
    app.run(debug=True)
