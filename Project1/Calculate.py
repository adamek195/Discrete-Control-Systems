from typing import List

#liczenie wartości funkcji celu
def calculate(r : List[int], p: List[int], q: List[int], taskNumber):
    S = [] #wektor rozpoczecia kolejnych zadan
    C = [] #wektor momentow zakończenia zadan
    Cq = [] #wektor mementów zakończenia i ostygnięcia zadań 
    S.append(max(r[0],0))
    C.append(S[0]+p[0])
    Cq.append(C[0]+q[0])
    Cmax = C[0]+q[0]
    for j in range(1, taskNumber):
        S.append(max(r[j], C[j-1]))
        C.append(S[j]+ p[j])
        Cq.append(C[j]+q[j])
        Cmax = max(Cmax, Cq[j])
    return S, C, Cq, Cmax
