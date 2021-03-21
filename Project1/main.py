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
    
    A = 0
    # X = 29
    for number in p:
        A += number
    
    for task in tasks:
        r.append(generator.nextInt(1,A))

    for task in tasks:
        q.append(generator.nextInt(1,A))

    print("nr:", nr)
    print("r: ", r)
    print("p: ", p)
    print("q: ", q)
    print("\n")

    S, C, Cq, Cmax = calculate(r,p,q, taskNumber)
    print("S: ", S)
    print("C: ", C)
    print(f"Cq: {Cq}")   
    print("Cmax", Cmax)
    print("\n")


    #inicjalizacja permutacji zadań
    pi = nr.copy()

    #strutktura skladajaca sie z 
    solution = []
    for task in tasks: 
        solution.append([pi[task-1], r[task-1], p[task-1], q[task-1]])

    #Schrage 
    print("Schrage:")
    pi = schrage(r, p, q, tasks)
    sort = {x: i for i, x in enumerate(pi)}
    solution.sort(key = lambda x: sort[x[0]])
    print("pi:", pi)
  
    rjSchrage = []
    pjSchrage = []
    qjSchrage = []

    for task in tasks:
        rjSchrage.append(solution[task-1][1])
        pjSchrage.append(solution[task-1][2])
        qjSchrage.append(solution[task-1][3])

    SSchrage, CSchrage, CqSchrage, CmaxSchrager = calculate(rjSchrage, pjSchrage, qjSchrage, taskNumber) 
    print("S: ", SSchrage)
    print("C: ", CSchrage)
    print(f"Cq: {CqSchrage}")     
    print("Cmax", CmaxSchrager)
    
    # Schrage z prerwaniami 
    # pi = nr.copy()
    # print("\nSchrage z przerwaniami")
    # pi = schragePmtn(rj, pj, qj, numberTasks)

    # sort = {x: i for i, x in enumerate(pi)}
    # solution.sort(key = lambda x: sort[x[0]])
    # print("pi:", pi)

    # rjSchragePmtn = []
    # pjSchragePmtn = []
    # qjSchragePmtn = []

    # for task in numberTasks:
    #     rjSchragePmtn.append(solution[task-1][1])
    #     pjSchragePmtn.append(solution[task-1][2])
    #     qjSchragePmtn.append(solution[task-1][3])

  
    # Cmax = calculate(rjSchragePmtn, pjSchragePmtn, qjSchragePmtn, maxTaskNumber)[2]  
    # print("Cmax", Cmax)

if __name__ == '__main__':
	main()
