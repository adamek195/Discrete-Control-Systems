from typing import List
import math

#implementacja algorytmu Schrage
def schrage(rj : List[int], pj: List[int], qj: List[int], numberTasks):
    #numer zadania w permutacji
    k = 1
    # zbiór zadań gotowych do realizacji
    G = []
    #zbiór zadań nieuszeregowanych
    N = list(numberTasks)
    #permutacja zadań
    pi = []
    #zmienna pomocnicza symbolizującą chwilę czasową
    t = min(rj)
    while len(G) or len(N):
        while len(N) and ( min(rj) <= t):
            j = rj.index(min(rj))
            #upewniamy sie ze tej wartosci juz nie uzyjemy
            rj[j] = 999999999
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




