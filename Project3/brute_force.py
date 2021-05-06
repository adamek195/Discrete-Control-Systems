import itertools
import sys

from calculate import target_fun

def brute_force(pj,wj,dj,taskNumber):
    comb=list(itertools.permutations(range(1,taskNumber+1)))
    F_solution = sys.maxsize

    for i in range(len(comb)):
        pj_i = []
        wj_i = []
        dj_i = []
        for j in range(len(comb[i])):
            pj_i.append(pj[comb[i][j]-1])
            wj_i.append(wj[comb[i][j]-1])
            dj_i.append(dj[comb[i][j]-1])
        target = target_fun(pj_i,wj_i,dj_i,len(comb[i]))
        if target < F_solution:
            F_solution = target
    return F_solution