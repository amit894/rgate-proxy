import os
from config import Config
from file import file_read_json

def get_proxy_stats():
    return (file_read_json("../config/stats.json"))
