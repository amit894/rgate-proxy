from flask import Flask,request,redirect,Response,jsonify
import requests

from file import file_read
from file import file_read_match
from file import file_yaml_key


app = Flask(__name__)

@app.route("/")
def index():
    response = Response(file_yaml_key("default_response","../config.yaml")["body"], file_yaml_key("default_response","../config.yaml")["status_code"])
    return response

@app.route("/stats")
def stats():
    stats=file_read("../config/stats.json")
    return jsonify(stats)

@app.route("/<path:path>",methods=["GET","POST","DELETE"])
def proxy(path):
    global SITE_NAME
    if request.method=="GET":
        SITE_NAME=(file_read_match(path.split("/")[0],"../config/docker_path.yml"))
        print(SITE_NAME)
        if (SITE_NAME!=None):
            resp = requests.get(SITE_NAME)
            response = Response(resp.content, resp.status_code)
            return response
        else:
            response = Response(file_yaml_key("default_response","../config.yaml")["body"], file_yaml_key("default_response","../config.yaml")["status_code"])
            return response

    elif request.method=="POST":
        resp = requests.post(SITE_NAME,json=request.get_json())
        response = Response(resp.content, resp.status_code)
        return response
    else:
        response = Response(resp.content,"405")

if __name__ == "__main__":
    app.run(debug = False,port=8080)
