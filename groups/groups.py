
class Cond:
    def __init__(self,cond, iscomp=False):
        self.cond = cond
        self.iscomp = iscomp
    def e(self,x): #evaluate condition on x
        if not self.iscomp:
            return self.cond(x)
        return not self.cond(x)
        
class Group:
    def __init__(self,cond,condn = None ,iscomp = False, condU = None):
        #cond -> Any of these conditions must be met to include in the set
                 #must be a function that returns a bool
        #condn -> All of these conditions must be met to include in the set
        #condU -> All elements must met this condition to be included in the set
        
        self.condU=condU#Condicion del universo
        if not condn:
            self.condn=[]
        else:
            self.condn = condn
        
        if not isinstance(cond,Cond) and not isinstance(cond,list):
            cond = Cond(cond)
        if isinstance(cond,list):
            self.cond = cond
        else:
            self.cond = [cond]
            
            
            
        self.iscomp = iscomp
        
    def contiene(self,x):
        statements = []
        
        
        flag = True #-> This flag must be true all the time for x to be in the set
        if isinstance(x,set):
            for cond in self.cond:
                statements.append(all([cond.e(i) for i in x]))
                
            if self.condU is not None:
           
                flag = (all([self.condU.e(i) for i in x]))
                
           
                
        else:
            for cond in self.cond:
                statements.append(cond.e(x))   
            if self.condU is not None:
                
                flag = self.condU.e(x)
           
         
        if not flag:
            return False
                
        if not self.iscomp:
            isin= any(statements)
        else:
            isin= not any(statements)
            
            
        if self.condn:
            
            statements2=[]
            
            if isinstance(x,set):
                
                for cond in self.condn:
                    statements2.append(all([cond.e(i) for i in x]))           
            else:
                
                for cond in self.condn:
                    
                    statements2.append(cond.e(x)) 

           
            if not flag:
                return False
                    
            if not self.iscomp:
                isin= all(statements2)
            else:
                isin= not all(statements2)
        return isin
    def complemento(self):
      
        return Group([Cond(x.cond, iscomp = True) for x in self.cond],
                     condn=[Cond(x.cond, iscomp = True) for x in self.condn]
                     , condU=self.condU)
    
    
    def interseccion(self,x):
        return Group(self.cond.copy(),
                     condn = self.cond.copy()+x.cond.copy() ,
                    
                     condU=self.condU)
    
    def union(self,x):
        
        return Group(self.cond.copy()+x.cond.copy(), condU=self.condU)
    def examples(self,rng,start=0):
        #Prints some examples of the items in the group
        temp = start
        ex = []
        while len(ex)<rng:
            if self.contiene(temp):
                ex.append(temp)
            temp+=1
        return ex
        
        
    
"""
grupo = Grupo(lambda x: (x%2==0 and x>0 ))
grupo_ = grupo.complemento()
grupo2 = Grupo(lambda x: (x%2!=0 and x>-5))
grupo3 = grupo.union(grupo2)


#print(grupo.contiene({4,6,8,11}))
#print(grupo_.contiene(13))
print(grupo.contiene(4))
print(grupo3.contiene(-3))
"""
U = Group(lambda x: (x>0 and isinstance(x,int)))

X = Group(lambda x: (x>0 and x<=5 and isinstance(x,int)), condU=U.cond[0])
#print(X.contiene({1,2,3,4,5}))
#print(X.contiene({1,2,3,4,5,6}))

Y = Group(lambda x: x%2==0 and x>0,  condU=U.cond[0])
print(X.contiene(1))

X_ = X.complemento()
print(X_.contiene(10))
#print(X_.contiene({1,2,3,4,5}))
#print(X_.contiene(8))
#print(X_.contiene(8.5))
#Punto 18----
#XnY = X.interseccion(Y)
#print(XnY.contiene(6))
#print(X_.condU)
X_nY = X_.interseccion(Y)
Y_ = Y.complemento()
print(X_nY.contiene(8))
XnY_  = Y_.interseccion(X)
print(XnY_.contiene(3))
X_nY_=X_.interseccion(Y)
print(X_nY_.contiene(12))
print(X_nY_.examples(100))





















