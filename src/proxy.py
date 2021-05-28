from flask import Flask,request,redirect,Response,jsonify
import requests

from file import file_read_json
from file import search_key_json
from file import search_key_yaml
from docker import Docker


@app.route("/")
def index():
    response = Response(search_key_yaml("default_response","../config.yaml")["body"], search_key_yaml("default_response","../config.yaml")["status_code"])
    return response

@app.route("/stats")
def stats():
    stats=file_read_json("../config/stats.json")
    return jsonify(stats)

@app.route("/<path:path>",methods=["GET","POST"])
def proxy(path):
    global backend_name
    if request.method=="GET":
        backend_name=(search_key_json(path.split("/")[0],"../config/docker_path.yml"))
        print(Docker.select_backend(path.split("/")[0]))
        if (backend_name!=None):
            resp = requests.get(backend_name)
            response = Response(resp.content, resp.status_code)
            return response
        else:
            response = Response(search_key_yaml("default_response","../config.yaml")["body"], search_key_yaml("default_response","../config.yaml")["status_code"])
            return response

    elif request.method=="POST":
        backend_name=(search_key_json(path.split("/")[0],"../config/docker_path.yml"))
        print(backend_name)
        if (backend_name!=None):
            resp = requests.post(backend_name,json=request.get_json())
            response = Response(resp.content, resp.status_code)
            return response
        else:
            response = Response(search_key_yaml("default_response","../config.yaml")["body"], search_key_yaml("default_response","../config.yaml")["status_code"])
            return response
    else:
        response = Response("Method not supported","405")

if __name__ == "__main__":
    app.run(debug = False,port=8080)
