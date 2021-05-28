import os
import re
from config import Config
import numpy as np
from file import file_read_json

class Stats():
    def __init__(self):
        pass

    log_file="../logs/rgate.log"

    @staticmethod
    def get_proxy_stats():
        request_stats={"success":0,"failure":0}
        response_stats={"average":0,"p95":0,"p99":0}
        temp_response_time=[]
        file=open(Stats.log_file)
        for lines in (file):
            log = re.split("-",lines)
            if (int(log[0])>399):
                request_stats["failure"]+=1
            else:
                temp_response_time.append(float(log[1].strip()))
                request_stats["success"]+=1
        return(Stats.calculate_proxy_stats(request_stats,response_stats,temp_response_time))

    @staticmethod
    def calculate_proxy_stats(request_stats,response_stats,temp_response_time):
        stats={}
        response_stats["average"]=np.percentile(temp_response_time, 50)
        response_stats["p95"]=np.percentile(temp_response_time, 95)
        response_stats["p99"]=np.percentile(temp_response_time, 99)
        stats["request_count"]=request_stats
        stats["latency_ms"]=response_stats
        return stats


#print(Stats.get_proxy_stats())
