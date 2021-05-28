import json
import yaml

def search_key_json(match_key,path):
    f1=open(path)
    file_json=json.load(f1)
    for key in file_json:
        if key==match_key:
            return(file_json[key])
    f1.close()

def file_read_json(path):
    f1=open(path)
    file_json=json.load(f1)
    f1.close()
    return file_json

def file_write(path,string):
    f1=open(path,"a")
    f1.write(string+"\n")
    f1.close()

def search_key_yaml(key,path):
    f1 = open(path)
    input_list = yaml.load(f1, Loader=yaml.FullLoader)
    f1.close()
    return(input_list[key])
