from Calculate import calculate
from RandomNumberGenerator import RandomNumberGenerator
from Schrage import schrage
from SchragePmtn import schragePmtn



def main():
    seed = int(input("Wprowadź Z:"))
    generator = RandomNumberGenerator(seed)
    taskNumber = int(input("Wprtowadź liczbe zadań:"))
    tasks = range(1, taskNumber+1)

    nr = []  #wektor kolejnych zadan
    r = []  #czas przygotowania kolejnych zadań
    p = []  #czas wykonania kolejnych zadan
    q = []  #czas dostarczenia/stygnięcia kolejnych zadań

    #generowanie danych do zadania
    for task in tasks:
        nr.append(task)
        p.append(generator.nextInt(1,29))

    pi = nr.copy() #inicjalizacja permutacji zadań

    A = 0
    # X = 29
    for number in p:
        A += number

    for task in tasks:
        r.append(generator.nextInt(1,A))

    for task in tasks:
        q.append(generator.nextInt(1,29))

    print("\nnr:", nr)
    print("r: ", r)
    print("p: ", p)
    print("q: ", q)
    print("\n")

    S, C, Cq, Cmax = calculate(r,p,q, taskNumber)
    print(f'pi: {pi}')
    print("S: ", S)
    print("C: ", C)
    print(f"Cq: {Cq}")
    print("Cmax", Cmax)
    print("\n")


    #inicjalizacja permutacji zadań
    # pi = nr.copy()

    #strutktura skladajaca sie z
    solution = []
    for task in tasks:
        solution.append([pi[task-1], r[task-1], p[task-1], q[task-1]])

    #Schrage
    print("Po sortowaniu:")
    pi = schragePmtn(r, p, q, tasks)
    sort = {x: i for i, x in enumerate(pi)}
    solution.sort(key = lambda x: sort[x[0]])

    rjSchrage = []
    pjSchrage = []
    qjSchrage = []

    for task in tasks:
        rjSchrage.append(solution[task-1][1])
        pjSchrage.append(solution[task-1][2])
        qjSchrage.append(solution[task-1][3])

    SSchrage, CSchrage, CqSchrage, CmaxSchrager = calculate(rjSchrage, pjSchrage, qjSchrage, taskNumber)
    print("pi:", pi)
    print("S: ", SSchrage)
    print("C: ", CSchrage)
    print(f"Cq: {CqSchrage}")
    print("Cmax", CmaxSchrager)


if __name__ == '__main__':
	main()


