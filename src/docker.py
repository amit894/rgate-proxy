from file import search_key_yaml
from command import Command

class Docker:
    def __init__(self):
        pass

    @staticmethod
    def backend_exists(match_backend,backends):
        for backend in backends:
            if backend["name"]==match_backend:
                return True
        return False

    @staticmethod
    def search_backend(name,backends):
        return [backend for backend in backends if backend['name'] == name]

    @staticmethod
    def select_backend(match_backend):
        backends=file_yaml_key("backends","../config.yaml")
        if Docker.backend_exists(match_backend,backends):
            backend=Docker.search_backend(match_backend,backends)
            Docker.list_backend_containers(backend[0]["match_labels"])
        else:
            print("backend Doesn't Exits")

    @staticmethod
    def list_backend_containers(match_labels):
        filter_expression=""
        for label in match_labels:
            filter_expression+="--filter label="+label+" "
        if (Command.run_command("docker ps",filter_expression)):
            print("Service Execution has Errors")
        else:
            print("Service Execution is succesful")

    @staticmethod
    def run_service(path):
        arg=path+" && docker-compose up"
        if (Command.run_command("cd",arg)):
            print("Service Execution has Errors")
        else:
            print("Service Execution is succesful")
