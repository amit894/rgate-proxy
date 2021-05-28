from flask import Flask,request,redirect,Response,jsonify
import requests
from logger import Logger

from file import file_read_json
from file import search_key_json
from file import search_key_yaml
from stats import Stats

DEFAULT_RESPONSE_TIME=0.05

app = Flask(__name__)

@app.route("/")
def index():
    response = Response(search_key_yaml("default_response","../config.yaml")["body"], search_key_yaml("default_response","../config.yaml")["status_code"])
    Logger.write()
    return response

@app.route("/stats")
def stats():
    stats=Stats.get_proxy_stats()
    return jsonify(stats)

@app.route("/<path:path>",methods=["GET","POST"])
def proxy(path):
    global backend_name
    if request.method=="GET":
        backend_name=(search_key_json(path.split("/")[0],"../config/docker_path.yml"))
        if (backend_name!=None):
            resp = requests.get(backend_name)
            #print(resp.status_code,resp.elapsed.total_seconds())
            response = Response(resp.content, resp.status_code)
            Logger.write(resp.status_code,resp.elapsed.total_seconds())
            return response
        else:
            default_response=search_key_yaml("default_response","../config.yaml")
            response = Response(default_response["body"],default_response["status_code"])
            Logger.write(default_response["status_code"],DEFAULT_RESPONSE_TIME)
            return response

    elif request.method=="POST":
        backend_name=(search_key_json(path.split("/")[0],"../config/docker_path.yml"))
        if (backend_name!=None):
            resp = requests.post(backend_name,json=request.get_json())
            Logger.write(resp.status_code,resp.elapsed.total_seconds())
            Logger.write()
            return response
        else:
            default_response=search_key_yaml("default_response","../config.yaml")
            response = Response(default_response["body"],default_response["status_code"])
            Logger.write(default_response["status_code"],DEFAULT_RESPONSE_TIME)
            return response
    else:
        response = Response("Method not supported","405")
        Logger.write()


if __name__ == "__main__":
    app.run(debug = False,port=8080)
