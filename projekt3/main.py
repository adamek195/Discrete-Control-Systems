from RandomNumberGenerator import RandomNumberGenerator
import itertools
import sys
import numpy as np

def main():
    seed = int(input("Wprowadź Z: "))
    generator = RandomNumberGenerator(seed)
    taskNumber = int(input("Wprowadź rozmiar problemu: "))
    tasks = range(1, taskNumber+1)
    nr=[]
    pj=[] #czas wykonania
    wj=[] #waga/współczynnik kary
    dj=[] #żądany termin zakończenia

    for task in tasks:
        nr.append(task)
        pj.append(generator.nextInt(1,29))

    A = 0
    for number in pj:
        A += number

    for task in tasks:
        wj.append(generator.nextInt(1,9))
    X = 29
    #X=A
    for task in tasks:
        dj.append(generator.nextInt(1,X))

    print("\nnr:", nr)
    print("pj: ", pj)
    print("wj ", wj)
    print("dj", dj)
    print("\n")

    print(f'F={target_fun(pj,wj,dj,taskNumber)}')
    print(f'F={brute_force(pj,wj,dj,taskNumber)}')


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

def brute_force(pj,wj,dj,taskNumber):
    comb=list(itertools.permutations(range(1,taskNumber+1)))
    F_wynik = sys.maxsize

    for i in range(len(comb)):
        pj_i = []
        wj_i = []
        dj_i = []
        for j in range(len(comb[i])):
            pj_i.append(pj[comb[i][j]-1])
            wj_i.append(wj[comb[i][j]-1])
            dj_i.append(dj[comb[i][j]-1])
        target = target_fun(pj_i,wj_i,dj_i,len(comb[i]))
        if target < F_wynik:
            F_wynik = target
    return F_wynik

if __name__ == '__main__':
	main()
