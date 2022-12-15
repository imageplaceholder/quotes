import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['isDirectory'] = "true"
        d['content'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['isDirectory'] = "false"
        d['size'] = 0
    return d

data = path_to_dict('.')


def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

write_json("test-tree.json", data)  
        
