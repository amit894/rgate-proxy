import os
import yaml
import json
import jinja2
from docker import Docker
from config import Config


docker_compose_master_dict= dict({"version": '3'})


class Deployer():
    def __init__(self,config,docker):
        self.docker=docker
        self.config=config

    def read_config(self):
        file = open(self.config.file)
        input_list = yaml.load(file, Loader=yaml.FullLoader)
        self.backend_list=input_list["backends"]
        file.close()

    def get_compose_config(self):
        return (self.config.path+"docker-compose.yml")

    def get_docker_config(self):
        return (self.config.path+"docker_path.yml")

    def deploy_rgate(self):
        self.read_config()
        self.create_service()
        self.docker.run_service(self.config.path)
        self.create_backend_map()

    def create_service(self):
        host_port=80
        backend_list={}
        compose_file = open(self.get_compose_config(),"w")
        for backend in self.backend_list:
            temp_service={}
            temp_service["image"]="amit894/"+backend["name"]+":1.0.0"
            temp_service["ports"]=(str(host_port)+":80").split()
            temp_service["container_name"]=backend["name"]+"-service"
            temp_service["hostname"]=backend["name"]+"-service"
            temp_service["labels"]=["app_name="+backend["name"],"env=production"]
            backend_list[backend["name"]]=temp_service
            host_port+=1
        docker_compose_master_dict["services"]=backend_list
        yaml.dump(docker_compose_master_dict,compose_file)
        compose_file.close()

    def create_backend_map(self):
        path_list={}
        host_port=80
        dockers_path = open(self.get_docker_config(),"w")
        for backend in self.backend_list:
            path_list[backend["name"]]="http://localhost:"+str(host_port)+"/"
            host_port+=1
            print(self.docker.select_backend(backend["name"]))
        json.dump(path_list,dockers_path)
        dockers_path.close()


D1=Deployer(Config(),Docker())
D1.read_config()
D1.create_backend_map()
