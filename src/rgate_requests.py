import requests
from flask import Flask,request,redirect,Response,jsonify
from config import Config
from logger import Logger
from file import file_read_json
from file import search_key_json
from file import search_key_yaml

class RGate_Requests():
    def __init__(self):
        pass

    config=Config()
    default_response_key="default_response"
    default_response_time=0.05
    dockers_path=config.path+"docker_path.json"

    @staticmethod
    def default_response():
        default_response=search_key_yaml(RGate_Requests.default_response_key,RGate_Requests.config.file)
        response = Response(default_response["body"],default_response["status_code"])
        Logger.write(default_response["status_code"],RGate_Requests.default_response_time)
        return response

    @staticmethod
    def get_method(path):
        backend_name=(search_key_json(path.split("/")[1],RGate_Requests.dockers_path))
        if (path.split("/")[0]=="api" and backend_name!=None):
            try:
                resp = requests.get(backend_name)
                response = Response(resp.content, resp.status_code)
                Logger.write(resp.status_code,resp.elapsed.total_seconds())
                return response
            except:
                response = Response("Backend Down",503)
                Logger.write(503,RGate_Requests.default_response_time)
                return response
        else:
            return RGate_Requests.default_response()

    @staticmethod
    def post_method(path):
        backend_name=(search_key_json(path.split("/")[0],RGate_Requests.dockers_path))
        if (path.split("/")[0]=="api" and backend_name!=None):
            try:
                resp = requests.post(backend_name,json=request.get_json())
                response = Response(resp.content, resp.status_code)
                Logger.write(resp.status_code,resp.elapsed.total_seconds())
                return response
            except:
                response = Response("Backend Down",503)
                Logger.write(503,RGate_Requests.default_response_time)
                return response
        else:
            return RGate_Requests.default_response()

#RGate_Requests.default_response()
