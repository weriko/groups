import itertools
class Node:
  def __init__(self, nodes, prob=0, name=None, level=0, parent=None):
    self.prob = prob
    self.nodes = nodes
    self.name = name
    self.level=level
    self.parent = parent
  def add_node(self,node):
    node.parent = self
    self.nodes.append(node)
  def is_exhaustive(self):
    if not self.nodes:
      return True
    if  not sum([x.prob for x in self.nodes])==1:
      return False
    return all([x.is_exhaustive() for x in self.nodes])
  def show(self):
    print(self)
    for i in self.nodes:
      i.show()
  def __repr__(self):
    return self.level*"|--"+f"{self.name} ({self.prob})"

  def flatten(self):
    a = []
    a.append(self)
    p=[]
    for i in self.nodes:
      p.extend(i.flatten())
    a.extend(p)
    return a
  def find_by_name(self,name):
    return [x for x in self.flatten() if x.name==name]
      



  @staticmethod
  def parse_dict(d,lev =0, root=None):
    if not root:
      root=Node([],name="root")
  
    for k,v in d.items():
      if isinstance(v,dict):
        n = Node([],name=k,prob=v.get("prob"), level=lev+1)
        root.add_node(n)
        Node.parse_dict(v,root=n,lev=lev+1)
     

    if lev==0:
      return root
  def mult_by_parent(self):
    return self.prob*self.parent.prob
  
d = {"E":{
        "prob":0.005,
        "PP":{"prob":0.99},
        "PN":{"prob":0.01}
},
     "NE":{
        "prob":0.995,
        "PP":{"prob":0.01},
        "PN":{"prob":0.99}
},}

def require_exhaustive(func):
  def wrapper(*args,**kwargs):
    try:
      n = args[0]
      
      if n.is_exhaustive():
        pass
      else:
        raise ValueError("Not exhaustive")
    except:
      n = kwargs.get("node",None)
      if n.is_exhaustive():
        pass
      else:
        raise ValueError("Not exhaustive")
  return wrapper




def bayes(node=None, PAname=None, PBname=None):

  
  PA = node.find_by_name(PAname)
  PB = node.find_by_name(PBname)
  idx = next((i for i,x in enumerate(node.nodes) if x.name == PAname), None)

  s = sum([x.mult_by_parent() for x in PB])
  
  return PA[0].prob*PB[idx].prob/s
  



  
  

nodes = [Node([],prob=0.3), Node([],prob=0.7)]
n = Node(nodes, name="root")
#print(n.is_exhaustive())
#print(d)
t = Node.parse_dict(d)

#t.show()
#print(t.is_exhaustive())
#print(t.find_by_name("Azul"))

bayes(t, PAname = "NE", PBname = "PP")
