from typing import List
from decimal import Decimal


def schragePmtn(rj : List[int], pj: List[int], qj: List[int], numberTasks):
    # zbiór zadań gotowych do realizacji
    G = []
    #zbiór zadań nieuszeregowanych
    N = list(numberTasks)
    #aktualne zadanie majace mniejszy czas dostarczenia q
    l = 0
    #zmienna pomocnicza symbolizującą chwilę czasową
    t = 0
    #permutacja zadań
    pi = []
    #przypisanie pierwszemu czasu dostarczenia nieskonczony czas
    qj[0] = 999999999
    while len(G) or len(N):
        while len(N) and ( min(rj) <= t):
            j = rj.index(min(rj))
            #upewniamy sie ze tej wartosci juz nie uzyjemy
            rj[j] = 999999999 
            G.append(j+1)
            N.remove(j+1)
            #obsluga przerwań
            if qj[j] > qj[l]:
                pj[l] = t - rj[j]
                t = rj[j]
                if pj[l] > 0:
                    G.remove(j+1)    
        if len(G):
            j = qj.index(max([qj[i - 1] for i in G])) + 1
            #upewniamy sie ze tej wartosci juz nie uzyjemy        
            qj[j -1] = -999999999
            G.remove(j)
            pi.append(j)
            t += pj[j-1]
            l = j-1
        else:
            t = min(rj)
    return pi        