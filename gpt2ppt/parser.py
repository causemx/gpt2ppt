import json
from utils import IterWrapper


def parse(json_input, prefix=0):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if len(json_input) == 1:
                print(f"{k} : {v}, {prefix}")
            else:
                print(f"{k}, {prefix}")
                parse(v, prefix=prefix+1)
    elif isinstance(json_input, list):
        for item in json_input:
            print(f"{item}, {prefix}")
            parse(item, prefix+1)

# Find specific key-value recursively
#* dict_var: json doc
def id_generator(dict_var):
    for k, v in dict_var.items():
        if k == "id":
            yield v
        elif isinstance(v, dict):
            for id_val in id_generator(v):
                yield id_val

if __name__ =="__main__":
    with open("input/input.json") as topo_file:
        parse(json.load(topo_file))