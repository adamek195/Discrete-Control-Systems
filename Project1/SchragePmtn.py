from typing import List
from decimal import Decimal


def schragePmtn(r : List[int], p: List[int], q: List[int], numberTasks):
    Cmax = 0 
    G = [] # zbiór zadań gotowych do realizacji
    N = list(numberTasks) #zbiór zadań nieuszeregowanych
    t = 0 #zmienna pomocnicza symbolizującą chwilę czasową
    l = 0 #aktualne zadanie majace mniejszy czas dostarczenia q
    q[0] = 999999999 #przypisanie pierwszemu czasu dostarczenia nieskonczony czas
    pi = [] #permutacja zadań
    while len(G) or len(N):
        while len(N) and ( min(r) <= t):
            j = r.index(min(r))
            r[j] = 999999999  #upewniamy sie ze tej wartosci juz nie uzyjemy
            G.append(j+1)
            N.remove(j+1)
            #obsluga przerwań
            if q[j] > q[l]:
                p[l] = t - r[j]
                t = r[j]
                if p[l] > 0:
                    G.remove(j+1)    
        if len(G):
            j = q.index(max([q[i - 1] for i in G])) + 1
            q[j -1] = -999999999 #upewniamy sie ze tej wartosci juz nie uzyjemy 
            G.remove(j)
            pi.append(j)
            t += p[j-1]
            l = j-1
        else:
            t = min(r)
    return pi        