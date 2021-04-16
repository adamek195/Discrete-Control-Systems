def findmin(pj):
    values, idx2 = [], []
    for idx1 in range(len(pj)):
        values.append(min(pj[idx1]))
        idx2.append(pj[idx1].index(values[-1]))
    idx1 = values.index(min(values))
    return idx1, idx2[idx1]

def johson(tasks, pj):
    l = 0
    k = len(tasks) - 1
    tasks = list(tasks)
    N = tasks.copy()
    while (len(N)):
        j, i = findmin(pj)
        if pj[j][0] < pj[j][1]:
            tasks[l] = j + 1
            l += 1
        else:
            tasks[k] = j + 1
            k -= 1
        N.remove(j + 1)
        pj[j] = [9999999999,9999999999] # pj.remove(pj[j]) psuje findmin
    return tasks
