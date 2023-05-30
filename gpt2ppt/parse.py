import json
import queue

class Parser:
    def __init__(self) -> None:
        self.q = queue.Queue()
        
    def parse(self, json_input, prefix=0):
        if isinstance(json_input, dict):
            for k, v in json_input.items():
                if isinstance(v, str):
                    self.q.put(("{}:{}".format(k, v), prefix))
                    # print(f"{k} : {v}, {prefix} ohyeah") 
                else:
                    self.q.put((k, prefix))
                    self.parse(v, prefix=prefix+1)
        elif isinstance(json_input, list):
            for item in json_input:
                if not isinstance(item, dict):
                    self.q.put((item, prefix))
                self.parse(item, prefix+1)
    
    def dump(self):
        while not self.q.empty():
            print(self.q.get())

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
        p = Parser()
        p.parse(json.load(topo_file))