from Cond import Cond
from Diagram import Diagram

class Group:
    def __init__(self,cond ,iscomp = False, condU = None, name = None):
        #cond -> Any of these conditions must be met to include in the set
                 #must be a function that returns a bool
        #condU -> All elements must met this condition to be included in the set
        self.condU=condU#Universe condition
        self.name=name
        if not isinstance(cond,Cond):
            self.cond = Cond(cond)
        else:
            self.cond = cond
            
        self.iscomp = iscomp
        
    def contains(self,x):
                      
        statement = self.cond.e(x)
        statementU = True
        if self.condU:
            statementU = self.condU.cond.e(x)
        return statement and statementU
        
    def difference(self):
      
        return Group(Cond(self.cond.comp())
                     , condU=self.condU)

    def intersect(self,x):
        
        return Group(self.cond.And(x), condU=self.condU)
    
    def union(self,x):
        
        return Group(self.cond.Or(x), condU=self.condU)
    def examples(self,rng,start=0):
        #Prints some examples of the items in the group
      
        return [x for x in range(start,rng) if self.contains(x)]
    def __contains__(self,x):
        if isinstance(x,(set,list,tuple)):
            
            return all(self.contains(i) for i in x)
        else:
            return self.contains(x)
    def extract(self,x):
        return [i for i in x if i in self]
    def __add__(self,x):
        return self.union(x)
    def __radd__(self,x):
        return x.union(self)
    
    @staticmethod
    def get_all(s, *groups, plot=False): #could this be more efficient? maybe. returns members of all the intersections of n groups
        
        
        for i,x in enumerate(groups):
            if x.name is None:
                x.name=i #need to fix this
        names = [frozenset(i) for i in Diagram.powerset([x.name for x in groups])]
    
        t=[]
        for i in s:
            temp = []
            for g in groups:
                if i in g:
                    temp.append(g.name)
            if temp:
                t.append(frozenset(temp))
        
        c = {i:0 for i in names}
        for i in t:
            c[i]+=1
        if not plot:
            return c
        
        Diagram.create_diagram(len(groups),names=[x.name for x in groups], quantities=c)
