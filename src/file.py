import json
import yaml

def file_read_match(match_key,path):
    f1=open(path)
    file_json=json.load(f1)
    for key in file_json:
        if key==match_key:
            return(file_json[key])
    f1.close()

def file_read(path):
    f1=open(path)
    file_json=json.load(f1)
    f1.close()
    return file_json

def file_yaml_key(key,path):
    f1 = open(path)
    input_list = yaml.load(f1, Loader=yaml.FullLoader)
    f1.close()
    return(input_list["default_response"])
