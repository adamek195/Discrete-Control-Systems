from typing import List

#liczenie wartości funkcji celu
def calculate(pj, taskNumber, machineNumber):
    Sj = []
    Cj = []
    S = []
    C = []


    S.append(0)
    C.append(S[0]+pj[0][0])
    S.append(max(C[0], 0))
    C.append(S[1]+pj[0][1])
    for m in range(2, machineNumber):
        S.append(max(C[m-1],0))
        C.append(S[m]+pj[0][m])
    Sj.append(S.copy())
    S.clear()
    Cj.append(C.copy())
    C.clear()
    Cmax = Cj[0][1]

    for j in range(1, taskNumber):
        S.append(max(0,Cj[j-1][0]))
        C.append(S[0]+pj[j][0])
        for m in range(1, machineNumber):
            S.append(max(C[m-1],Cj[j-1][m]))
            C.append(S[m]+pj[j][m])
        Sj.append(S.copy())
        S.clear()
        Cj.append(C.copy())
        C.clear()
        Cmax = max(Cmax, Cj[j][machineNumber-1])
    return Sj, Cj, Cmax
