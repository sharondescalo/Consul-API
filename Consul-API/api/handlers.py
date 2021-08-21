from requests.exceptions import HTTPError
import requests,json
from typing import TypeVar, Generic

class respon:
    def __init__(self):
        self.status = 0
        self.message = 0
        self.payload = {}
    
    def serialize(self):
        return {
            'status': self.status, 
            'message': self.message,
        }
    def reprJSON(self):
        return dict(status=self.status, message=self.message, payload=self.payload) 

    def request_handler(self,url_suffix):
        # res = respon()
        try:
            # url = 'http://127.0.0.1:8500/v1/'+url_suffix
            url = 'http://10.199.0.10:8500/v1/'+url_suffix
            r = requests.get(url)
            r.raise_for_status()
        except HTTPError as http_err:
            self.status = 0
            self.status = format(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.status = 0
            self.message  = format(f'Other error occurred: {err}')
        else:
            self.status = 1
            self.message = 'payload OK'
            self.payload = r.json()
        return self
    
class summary(respon):
    def __init__(self):
        self.registered_nodes = 0
        self.registered_services = 0
        self.leader = 0
        self.cluster_protocol = 0

    def serialize(self):
        return {
            'status': self.status, 
            'message': self.message,
            'registered_nodes': self.registered_nodes, 
            'registered_services': self.registered_services,
            'leader': self.leader,
            'cluster_protocol': self.cluster_protocol,
        }
