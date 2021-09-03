class Cond:
    def __init__(self,cond, iscomp=False):
        self.cond = cond
        self.iscomp = iscomp
    def e(self,x): #evaluate condition on x
        return self.cond(x)
    def comp(self):
        return lambda x: not self.cond(x)
        
    def And(self,n):
        return lambda x: self.cond(x) and n.cond.cond(x) #Evaluates the first condition with the condition passed as argument 
    def Or(self,n):
        return lambda x: self.cond(x) or n.cond.cond(x)
