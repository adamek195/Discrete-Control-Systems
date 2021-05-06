from calculate import target_fun

def greedy(pj,wj,dj,taskNumber):
    calc = []
    for index, elem in enumerate(range(taskNumber)):
        calc.append([dj[index], pj[index], wj[index]])

    calc = sorted(calc, key=lambda x: x[0])
    pj, wj, dj = [], [], []
    for value in calc:
        dj.append(value[0])
        pj.append(value[1])
        wj.append(value[2])

    F_solution = target_fun(pj, wj, dj, taskNumber)

    return F_solution