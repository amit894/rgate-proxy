from flask import Flask,request,redirect,Response,jsonify
import requests
from rgate_requests import RGate_Requests
from logger import Logger

from file import file_read_json
from file import search_key_json
from file import search_key_yaml
from stats import Stats

DEFAULT_RESPONSE_TIME=0.05


app = Flask(__name__)


@app.route("/")
def index():
    return RGate_Requests.default_response()

@app.route("/stats")
def stats():
    stats=Stats.get_proxy_stats()
    return jsonify(stats)

@app.route("/<path:path>",methods=["GET","POST"])
def proxy(path):
    global backend_name
    if request.method=="GET":
        return RGate_Requests.get_method(path)
    elif request.method=="POST":
        return RGate_Requests.post_method(path)
    else:
        response = Response("Method not supported","405")
        Logger.write()

if __name__ == "__main__":
    app.run(debug = False,port=8080)
