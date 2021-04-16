from RandomNumberGenerator import RandomNumberGenerator
from Calculate import calculate
from Johson import johson

def main():
    # 2515 6 2
    seed = int(input("Wprowadź Z: "))
    generator = RandomNumberGenerator(seed)
    taskNumber = int(input("Wprtowadź liczbe zadań: "))
    tasks = range(1, taskNumber+1)
    machineNumber = int(input("Wprowadź liczbę maszyn: "))
    machines = range(1, machineNumber + 1)

    nr = []  #wektor kolejnych zadan
    pj = []
    pi = []
    solution = []
    p = []

    for task in tasks:
        for machine in machines:
            p.append(generator.nextInt(1, 29))
        pj.append(p.copy())
        p.clear()
        pi.append(task)

    print(pj)
    Sj, Cj, Cmax = calculate(pj,taskNumber,machineNumber)
    print("C", Cj)
    print("Cmax:", Cmax)

    for task in tasks:
        solution.append([pi[task-1], pj[task-1]])

    pi = johson(tasks, pj.copy())

    sort = {x: i for i, x in enumerate(pi)}
    solution.sort(key = lambda x: sort[x[0]])
    Sj, Cj, Cmax = calculate([row[1] for row in solution], taskNumber, machineNumber)
    print("C", Cj)
    print("Cmax:", Cmax)




if __name__ == '__main__':
	main()
