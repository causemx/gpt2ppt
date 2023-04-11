import json
from collections.abc import Iterator

def parse(doc) -> dict:
    try:
        j = json.load(doc)
        iter_j = hn_wrapper(j)
        while iter_j.hasnext():
            key = next(iter_j)
            if key.startswith('page'):  # ignore _comment token
                print(j[key]['title'])
                assert isinstance(j[key]['single_query'], str)
                assert isinstance(j[key]['array_query'], list) 
                assert isinstance(j[key]['multi_query'], dict)
                
    except FileNotFoundError as fe:
       print(str(fe))
    except TypeError as te:
       print(te)

class hn_wrapper(Iterator):  # need to subclass Iterator rather than object
  def __init__(self, it):
    self.it = iter(it)
    self._hasnext = None
    
  def __iter__(self): 
    return self
  
  def __next__(self):        # __next__ vs next in python 2
    if self._hasnext:
      result = self._thenext
    else:
      result = next(self.it)
    self._hasnext = None
    return result
  
  def hasnext(self):
    if self._hasnext is None:
      try: 
        self._thenext = next(self.it)
      except StopIteration: 
        self._hasnext = False
      else: self._hasnext = True
    return self._hasnext
