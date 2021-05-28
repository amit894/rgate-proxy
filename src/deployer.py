import os
import yaml
import json
import jinja2
from jinja2 import Template

docker_compose_master_dict= dict({"version": '3'})


class Deployer:
    def __init__(self,config):
        self.config_file_path=config

    def deploy_rgate(self):
        file = open(self.config_file_path)
        input_list = yaml.load(file, Loader=yaml.FullLoader)
        backend=input_list["backends"]
        file.close()
        self.create_service(backend)
        self.run_service()

    def create_service(self,backends):
        host_port=80
        temp_service_list={}
        path_list={}
        compose_file = open("../config/docker-compose.yml","w")
        dockers_path = open("../config/docker_path.yml","w")
        for backend in backends:
            temp_service={}
            temp_service["image"]="amit894/"+backend["name"]+":1.0.0"
            temp_service["ports"]=(str(host_port)+":80").split()
            temp_service["container_name"]=backend["name"]+"-service"
            temp_service["hostname"]=backend["name"]+"-service"
            temp_service["labels"]=["app="+backend["name"],"env=prod"]
            temp_service_list[backend["name"]]=temp_service
            path_list[backend["name"]]="http://localhost:"+str(host_port)+"/"
            host_port+=1
        docker_compose_master_dict["services"]=temp_service_list
        yaml.dump(docker_compose_master_dict,compose_file)
        json.dump(path_list,dockers_path)
        compose_file.close()
        dockers_path.close()

    def run_service(self):
        os.system(" cd ../config && docker-compose up")

D1=Deployer("../config.yaml")
D1.deploy_rgate()
