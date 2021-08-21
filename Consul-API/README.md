# Docker Flask API instructions
Build Dockerfile 
```bash
cd ./Consul-API/api/
docker build -t flask-api:latest .
```
Run Docker Container as shell:
```bash
docker run -it -p 5000:5000 flask-api
```

Docker log
```bash
docker container logs -f CONTAINER_ID
```

# Vagrant Consul Server instructions
Build Vagrant VM
```bash
cd ./Consul-API/consul-server/
vagrant up consul-server
```

## consul ui - login:
http://localhost:8500

## promethus ui - login:
http://localhost:8500


# Flask API - Use Example

## Status
```bash
curl http://localhost:5000/v1/api/consulCluster/status
systemInfo
```

example:
```bash
{
    "message": "Consul server is running",
    "status": 1
}
```
## Summary
```bash
curl http://localhost:5000/v1/api/consulCluster/summary
systemInfo
```

Example:
```bash
{
    "cluster_protocol": "3",
    "leader": "10.199.0.10:8300",
    "message": "payload OK",
    "registered_nodes": 1,
    "registered_services": 0,
    "status": 1
}
```

## Members
```bash
curl http://localhost:5000/v1/api/consulCluster/members
systemInfo
```

Example:
```bash
{
    "messgae": "payload OK",
    "registered_nodes": [
        "consul-server"
    ],
    "status": 1
}
```

## SystemInfo

```bash
curl http://localhost:5000/v1/api/consulCluster/systemInfo
```
Example:
```bash
{
    "CpuLoadAvaragePercent": [
        0.0,
        0.1708984375,
        0.0
    ],
    "DiskUsagePercent": 0.5,
    "DiskUsageTotalGB": 250.98248672485352,
    "NetworkIOCountersBytesReceived": 3.625,
    "NetworkIOCountersBytesSent": 1.8544921875,
    "swapMemoryUsedMB": 0.0,
    "vCpus": 4,
    "vMemoryAvailablePrecent": 90.04723023794298,
    "vMemoryTotalGB": 12.390636444091797,
    "vMemoryUsedMB": 659.37109375
}
```




