def Schrage_ptmn(tasks, rj, pj, qj):
    Ng = []
    tasks = list(tasks)
    Nn = tasks
    tasks = []
    l = 0 
    q0 = 99999999999
    t = 0
    Cmax = 0
    while (len(Ng)) or (len(Nn)):
        while (len(Nn)) and (min(rj) <= t):
            j = rj.index(min(rj))
            rj[j] = 99999999999
            Ng.append(j + 1)
            Nn.remove(j + 1)
            if qj[j+1] > qj[l]:
                pj[l] = t - rj[j+1]
                t = rj[j+1]
                if pj[l] > 0:
                    Ng.append(j + 1)            
        if len(Ng):
            j = qj.index(max([qj[i - 1] for i in Ng])) + 1
            qj[j - 1] = - 99999999999
            Ng.remove(j)
            l = j+1
            t += pj[j - 1]
            Cmax = max(Cmax, t + qj[j - 1])
        else:
            t = min(rj)
    return tasks

