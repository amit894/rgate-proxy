import json

def file_read_match(match_key,path):
    f1=open(path)
    file_json=json.load(f1)
    for key in file_json:
        if key==match_key:
            return(file_json[key])

def file_read(path):
    f1=open(path)
    file_json=json.load(f1)
    return file_json
