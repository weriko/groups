
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
        
class Group:
    def __init__(self,cond,condn = None ,iscomp = False, condU = None):
        #cond -> Any of these conditions must be met to include in the set
                 #must be a function that returns a bool
        #condU -> All elements must met this condition to be included in the set
        self.condU=condU#Condicion del universo
       
        if not condn:
            self.condn=[]
        else:
            self.condn = condn
        
        if not isinstance(cond,Cond):
            self.cond = Cond(cond)
        else:
            self.cond = cond
            
        self.iscomp = iscomp
        
    def contains(self,x):
                      
        statement = self.cond.e(x)
        statementU = True
        if self.condU:
            statementU = self.condU.e(x)
        return statement and statementU
            
        
    def complemento(self):
      
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
    def __add__(self,x):
        return self.union(x)
    def __radd__(self,x):
        return x.union(self)



U = Group(lambda x: (x>0 and isinstance(x,int)))

X = Group(lambda x: (x>0 and x<=5 and isinstance(x,int)), condU=U.cond)

Y = Group(lambda x: x%2==0 and x>0,  condU=U.cond)
#print(X.contains(1))

#Tests----
X_ = X.complemento()
#print(X_.contains(10))
#print(X_.contains({1,2,3,4,5}))
#print(X_.contains(8))
#print(X_.contains(8.5))
#Punto 18----
XnY = X.intersect(Y)
#print(XnY.contains(6))
#print(X_.condU)
X_nY = X_.intersect(Y)
Y_ = Y.complemento()
#print(X_nY.contains(8))
XnY_  = Y_.intersect(X)
XuY = X.union(Y)
#print(XnY_.contains(3))
X_nY_=X_.intersect(Y_)
X_uY = X_.union(Y)
XnY_ = Y_.intersect(X)
XuY_ = Y_.union(X)
X_uY_ = X_.union(Y_)
#print(X_nY_.contains(12))
print("Ejemplos de X: ", X.examples(100, start=-10))

print("Ejemplos de Y: ", Y.examples(100,start=-10))

print("18) Ejemplos de X_: ", X_.examples(100, start=-10))

print("19) Ejemplos de Y_: ", Y_.examples(100,start=-10))

print("20) Ejemplos de XnY: ", XnY.examples(100,start=-10))

print("21) Ejemplos de XuY: ", XuY.examples(100,start=-10))

print("22) Ejemplos de X_nY: ", X_nY.examples(100,start=-10))

print("23) Ejemplos de X_uY: ", X_uY.examples(100,start=-10))

print("24) Ejemplos de XnY_: ", XnY_.examples(100,start=-10))

print("25) Ejemplos de XuY_: ", XuY_.examples(100,start=-10))

print("26) Ejemplos de X_nY_: ", X_nY_.examples(100,start=-10))

print("27) Ejemplos de X_uY_: ", X_uY_.examples(100,start=-10))

#print(X_nY_.examples(100))

#Punto 38
print("Punto 38-------------")
B = Group(lambda x: (x>0 and x**2-1<=x))
print(B.examples(100))
#punto 37
print("Punto 37-------------")
B = Group(lambda x: (x**3-2*x**2-x+2==0))
print(B.examples(1000,start=-1000))
#punto 39
print("Punto 39-------------")
B = Group(lambda x: (x>0 and x<5 and isinstance(x,int)) )
C = Group(lambda x: (x>0 and x<10 and isinstance(x,int) and x%2==0) )
print("B -> ",B.examples(100))
print("C-> ",C.examples(100))
A = B.intersect(C)
print("A-> ",A.examples(100))

X = Group(lambda x: x in [1,2,3,4,5])
Y = Group(lambda x: x in [4,5,6,7,8] )
Z = Group(lambda x: x in [1,3,5,7,9])
XuY = X+Y
XuYnZ= XuY.intersect(Z)
print({2} in XuYnZ)
X = Group(lambda x: x>0)



















