import math

def Johnson(tasks, p_ij):
    l = 0
    k = len(tasks) - 1
    tasks = list(tasks)
    N = tasks.copy()
    while (len(N)):
        task_processes = []
        machine_index = []
        for j in range(len(p_ij)):
            task_processes.append(min(p_ij[j]))
            machine_index.append(p_ij[j].index(task_processes[-1]))
        j = task_processes.index(min(task_processes))
        if p_ij[j][0] < p_ij[j][1]:
            tasks[l] = j + 1
            l += 1
        else:
            tasks[k] = j + 1
            k -= 1
        N.remove(j + 1)
        p_ij[j] = [math.inf , math.inf]
    return tasks