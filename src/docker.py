from file import search_key_yaml
from command import Command

class Docker:
    def __init__(self):
        pass

    def backend_exists(self,match_backend,backends):
        for backend in backends:
            if backend["name"]==match_backend:
                return True
        return False

    def search_backend(self,name,backends):
        return [backend for backend in backends if backend['name'] == name]

    def select_backend(self,match_backend):
        backends=search_key_yaml("backends","../config.yaml")
        if self.backend_exists(match_backend,backends):
            backend=self.search_backend(match_backend,backends)
            self.list_backend_containers(backend[0]["match_labels"])
        else:
            print("backend Doesn't Exits")

    def list_backend_containers(self,match_labels):
        filter_expression=""
        for label in match_labels:
            filter_expression+="--filter label="+label+" "
        if (Command.run_command("docker ps",filter_expression)):
            print("Service Execution has Errors")
        else:
            print("Service Execution is succesful")

    def run_service(self,path):
        arg=path+" && docker-compose up"
        if (Command.run_command("cd",arg)):
            print("Service Execution has Errors")
        else:
            print("Service Execution is succesful")
