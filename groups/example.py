from Group import Group
from Cond import Cond
cards = [k for s in [[str(i)+j for i in range(1,11)] + [i+j for i in "JQK"] for j in "PDCT" ] for k in s]


U = Group(lambda x: (x in cards))


A = Group(lambda x: ("D" in x) or ("C" in x),condU=U)
print("Group A: ",A.extract(cards))
B = Group(lambda x: (("D" in x) and (any([i in x for i in "JQK"]))), condU = U)
print("Group B: " ,B.extract(cards))
C = Group(lambda x: ("1" in x) and ("0" not in x))
print("Group C: ", C.extract(cards))
AUC = A.union(C)
print("Group AUC: ", AUC.extract(cards))
AUB = A.union(B)
print("Group AUB: ", AUB.extract(cards))
BUC = B.union(C)
print("Group BUC: ", BUC.extract(cards))
BnC = B.intersect(C)
print("Group BnC: ", BnC.extract(cards))
AnC = A.intersect(C)
print("Group AnC: ", AnC.extract(cards))
AnB = A.intersect(B)
print("Group AnB: ", AnB.extract(cards))
A_=A.difference()
print("Group ~A: ", A_.extract(cards))
B_=B.difference()
print("Group ~B: ", B_.extract(cards))
C_=C.difference()
print("Group ~C: ", C_.extract(cards))
