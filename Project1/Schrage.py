from typing import List
from decimal import Decimal 

#implementacja algorytmu Schrage
def schrage(rj : List[int], pj: List[int], qj: List[int], numberTasks):
    k = 1 #numer zadania w permutacji
    G = [] # zbiór zadań gotowych do realizacji
    N = list(numberTasks) #zbiór zadań nieuszeregowanych
    pi = [] #permutacja zadań
    t = min(rj) #zmienna pomocnicza symbolizującą chwilę czasową
    while len(G) or len(N):
        while len(N) and ( min(rj) <= t):
            j = rj.index(min(rj))
            #upewniamy sie ze tej wartosci juz nie uzyjemy
            rj[j] = 99999999
            G.append(j+1)
            N.remove(j+1)
        if len(G):
            j = qj.index(max([qj[i - 1] for i in G])) + 1
            #upewniamy sie ze tej wartosci juz nie uzyjemy        
            qj[j -1] = -999999999
            G.remove(j)
            pi.append(j)
            t += pj[j-1]
            k += 1
        else:
            t = min(rj)
    return pi



