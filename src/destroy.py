from docker import Docker
from config import Config

class Destructor:
    def __init__(self,config,docker):
        self.docker=docker
        self.config=config

    def stop_rgate(self):
        self.docker.stop_service(self.config.path)

De1=Destructor(Config(),Docker())
De1.stop_rgate()
