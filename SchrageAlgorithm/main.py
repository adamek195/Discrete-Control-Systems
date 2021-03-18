from Calculate import calculate
from RandomNumberGenerator import RandomNumberGenerator
from Schrage import schrage


def main():
    #pobieramy ziarno Z
    seed = int(input("Wprowadź Z:"))
    #dla podanego ziarna wywolujemy konstruktor parametryczny
    generator = RandomNumberGenerator(seed) 
    #wprowadzamy liczbe zadan n
    maxTaskNumber = int(input("Wprtowadź liczbe zadań:"))
    #inicjalizacja listy zadan
    numberTasks = range(1, maxTaskNumber+1)
    #wektor kolejnych zadan
    nr = [] 
    #czas przygotowania kolejnych zadań
    rj = [] 
    #czas wykonania kolejnych zadan
    pj = [] 
    #czas dostarczenia/stygnięcia kolejnych zadań
    qj = []

    #dla pobranych ilości zadań n losujemy czas wykonania kolejnych zadań
    for task in numberTasks:   
        nr.append(task)
        pj.append(generator.nextInt(1,29))

    #suma kolejnych czasow wykonania zadan
    sumA = 0
    for number in pj:
        sumA += number

    #dla pobranych ilosci zadan przypisujemy kolejne czasy wykonania poszczególnych zadań
    for task in numberTasks:
        rj.append(generator.nextInt(1,sumA))
    
    for task in numberTasks:
        qj.append(generator.nextInt(1,sumA))

    #wypisanie zadań i kolejnych czasow zadań
    print("nr:", nr)
    print("rj: ", rj)
    print("pj: ", pj)
    print("qj: ", qj)
    print("\n")
    #funkcja celu dla nieposortowanej permutacji
    Cmax = calculate(rj,pj,qj, maxTaskNumber)
    print("Cmax", Cmax)
    print("\n")

    #inicjalizacja permutacji zadań
    pi = nr.copy()

    #strutktura skladajaca sie z 
    solution = []
    for task in numberTasks: 
        solution.append([pi[task-1],rj[task-1],pj[task-1],qj[task-1]])

    #algorytm Schrage do optymalizacji zadań
    pi = schrage(rj, pj, qj, numberTasks)

    #posorotwanie odpowiednich wektorów
    sort = {x: i for i, x in enumerate(pi)}
    solution.sort(key = lambda x: sort[x[0]])
    print("pi:", pi)

    #czyscimy wektory aby moc je ustawic po sortowaniu
    rj = []
    pj = []
    qj = []
    #przypisujemy posortowane wektory
    for task in numberTasks:
        rj.append(solution[task-1][1])
        pj.append(solution[task-1][2])
        qj.append(solution[task-1][3])

    #funckja celu dla posortowanych wektorow
    Cmax = calculate(rj,pj,qj, maxTaskNumber)  
    print("Cmax", Cmax)

if __name__ == '__main__':
	main()
