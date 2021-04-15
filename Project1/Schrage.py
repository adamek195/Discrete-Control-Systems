from typing import List
from decimal import Decimal 

#implementacja algorytmu Schrage
def schrage(r : List[int], p: List[int], q: List[int], numberTasks):
    N = list(numberTasks) #zbiór zadań nieuszeregowanych
    G = [] # zbiór zadań gotowych do realizacji
    t = min(r) #zmienna pomocnicza symbolizującą chwilę czasową
    k = 1 #numer zadania w permutacji
    pi = [] #permutacja zadań
    while len(G) or len(N):
        while len(N) and ( min(r) <= t):
            j = r.index(min(r))
            r[j] = 99999999 #upewniamy sie ze tej wartosci juz nie uzyjemy
            G.append(j+1)
            N.remove(j+1)
        if len(G):
            j = q.index(max([q[i - 1] for i in G])) + 1
            #upewniamy sie ze tej wartosci juz nie uzyjemy        
            q[j -1] = -999999999
            G.remove(j)
            pi.append(j)
            t += p[j-1]
            k += 1
        else:
            t = min(r)
    return pi



