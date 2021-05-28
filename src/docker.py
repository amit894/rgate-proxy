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
            return(self.list_backend_containers(backend[0]["match_labels"]))
        else:
            return("backend Doesn't Exits")

    def list_backend_containers(self,match_labels):
        filter_expression=""
        for label in match_labels:
            filter_expression+="--filter label="+label+" "
        filter_expression+=" --format={{.Names}}"
        return(Command.run_command_output("docker ps",filter_expression))

    def run_service(self,path):
        arg=path+" && docker-compose up -d" 
        if (Command.run_command("cd",arg)):
            return("Service Execution has Errors")
        else:
            return("Service Execution is succesful")

    def stop_service(self,path):
        arg=path+" && docker-compose down"
        if (Command.run_command("cd",arg)):
            return("Service Execution has Errors")
        else:
            return("Service Execution is succesful")
