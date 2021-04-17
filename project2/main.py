from RandomNumberGenerator import RandomNumberGenerator
from Calculate import calculate
from Johson import Johnson

def main():
    seed = int(input("Wprowadź Z: "))
    generator = RandomNumberGenerator(seed)
    taskNumber = int(input("Wprowadź liczbę zadań: "))
    tasks = range(1, taskNumber+1)
    machineNumber = int(input("Wprowadź liczbę maszyn: "))
    machines = range(1, machineNumber + 1)

    #lista wszystkich zadan na konkretnych maszynach
    p_ij = []
    # permutacja zadan
    pi = []
    # wyswietlenie rozwiazania po wykonaniu algorytmu optymalizacji
    solution = []
    #lista zadan przydzielonych do jednej maszyny
    pj = []

    for task in tasks:
        for machine in machines:
            pj.append(generator.nextInt(1, 29))
        p_ij.append(pj.copy())
        pj.clear()
        pi.append(task)

    print(p_ij)
    print("Permutacj naturalna: ")
    print("pi: ", pi)
    Cj, Cmax = calculate(p_ij,taskNumber,machineNumber)
    print("C:", Cj)
    print("Cmax:", Cmax)

    for task in tasks:
        solution.append([pi[task-1], p_ij[task-1]])

    pi = Johnson(tasks, p_ij.copy())
    print("Johnson: ")
    print("pi: ", pi)

    sort = {x: i for i, x in enumerate(pi)}
    solution.sort(key = lambda x: sort[x[0]])
    Cj, Cmax = calculate([row[1] for row in solution], taskNumber, machineNumber)
    print("C", Cj)
    print("Cmax:", Cmax)




if __name__ == '__main__':
	main()
