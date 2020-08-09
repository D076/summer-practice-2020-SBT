import json
import requests
from threading import Thread
from time import sleep


class GatewayConnector(Thread):
    def __init__(
        self,
        gateway_ip,
        gateway_port,
        service_ip,
        service_port,
        service_name,
        service_version,
        service_apis
        ):

        super().__init__()

        # Gateway address
        self.gateway_ip = gateway_ip
        self.gateway_port = gateway_port

        # Service info
        self.service_ip = service_ip
        self.service_port = service_port
        self.service_name = service_name
        self.service_version = service_version
        self.serivce_apis = service_apis

        self.instance_id = None
        self.ping_interval = None

        self.ready_to_ping = False

        # Set daemon thread
        self.daemon = True

    def run(self):
        while self.ready_to_ping:
            self.__ping()
            sleep(self.ping_interval / 1000)


    # Publish apis to gateway service
    def publish(self):
        data = {
            'address': 'http://' + self.service_ip,
            'port': self.service_port,
            'name_service': self.service_name,
            'version_service': self.service_version,
            'api': self.serivce_apis
        }

        try:
            response = requests.post(
                f'http://{self.gateway_ip}:{self.gateway_port}/gateway/publish',
                json.dumps(data),
                headers={'content-type': 'application/json'}
                )
        except:
            raise ConnectionError('No connection to gateway')
        
        if response.status_code == 200:
            response_data = response.json()

            self.instance_id = response_data['instance_id']
            self.ping_interval = response_data['ping_interval']
        else:
            raise ConnectionError


    def unpublish(self):
        try:
            response = \
                requests.get(f'http://{self.gateway_ip}:{self.gateway_port}/gateway/unpublish/{self.instance_id}')
        except:
            raise ConnectionError('No connection to gateway')

        if response.status_code == 200:
            self.ready_to_ping = False
        else:
            raise ConnectionError


    # Send ready state to gateway service
    def ready(self):
        if not self.instance_id is None:
            try:
                response = \
                    requests.get(f'http://{self.gateway_ip}:{self.gateway_port}/gateway/ready/{self.instance_id}')
            except:
                raise ConnectionError('No connection to gateway')

            if response.status_code == 200:
                self.ready_to_ping = True
            else:
                raise ConnectionError
        else:
            raise RuntimeError('Instance ID were not given')


    def __ping(self):
        try:
            response = \
                requests.get(f'http://{self.gateway_ip}:{self.gateway_port}/gateway/ping/{self.instance_id}')
        except:
            self.ready_to_ping = False
            raise ConnectionError('No connection to gateway')

        if response.status_code != 200:
            self.ready_to_ping = False
            raise ConnectionError