def target_fun(pj,wj,dj,taskNumber):
    S = []
    C = []
    T = []

    S.append(0)
    C.append(S[0]+pj[0])

    for task in range(1,taskNumber):
        S.append(C[task-1])
        C.append(S[task]+pj[task])

    for task in range(0,taskNumber):
        T.append(max(C[task]-dj[task],0))

    F=0
    for task in range(0,taskNumber):
        F += wj[task]*T[task]
    return F