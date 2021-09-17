import matplotlib.pyplot as plt
import numpy as np
import math
import itertools


class Diagram:
    @staticmethod
    def powerset(iterable):
        s = list(iterable)
        return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1,len(s)+1))
 
    
    @staticmethod
    def create_diagram(n, rad = 2,center=5, size=(25,25), circlerad = 0.3, names=None, quantities=None):
        #If used by a group it will accept a powerset of all the intersections of said groups, plotting their
        #quantities
        plt.rcParams["figure.figsize"] = size
        fig, ax = plt.subplots()
        angle = 2 * np.pi / n
        xy = [(center+rad*np.sin(i*angle),
              center+rad*np.cos(i*angle)) for i in range(n)]
        for i in xy:
            circle = plt.Circle(i,rad+circlerad, fill=False)
            ax.add_patch(circle)
        if names is None:
            names = range(len(xy))
        if quantities is None:
            quantities = {}
       
        xy_name = [(i, x[0], x[1]) for i,x in zip(names,xy)]
  
        all_circ = Diagram.powerset(xy_name)
        intersections = {}
        
        for x in all_circ:
            
            name = tuple(i[0] for i in x)
            xs = sum([i[1] for i in x])/len(x)
            ys = sum([i[2] for i in x])/len(x)

            
            plt.annotate("".join(str(name))+" "+str(quantities.get(frozenset(name),"")),
                         (xs, ys))
            plt.scatter(xs,ys,label=name)
        plt.show()
        
