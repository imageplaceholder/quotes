import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d

data = path_to_dict('.')


def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

write_json("test-tree.json", data)  
        
