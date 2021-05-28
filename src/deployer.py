import os
import yaml
import json
import jinja2
from jinja2 import Template

class Deployer:
    def __init__(self,config):
        self.config_file_path=config
        self.template_path="../resources/templates-jinja/"
        self.helm_path="../resources/helm/charts/"

    def deploy_rgate(self):
        file = open(self.config_file_path)
        input_list = yaml.load(file, Loader=yaml.FullLoader)
        routes=input_list["routes"]
        backend=input_list["backends"]
        file.close()

        self.create_ingress(routes)
        self.create_service(backend)

    def create_ingress(self,routes):
        temp_list=[]
        route_list=[]
        for route in routes:
            print(route)

    def create_service(self,backends):
        for backend in backends:
            print(backend)

D1=Deployer("../config.yaml")

D1.deploy_rgate()
