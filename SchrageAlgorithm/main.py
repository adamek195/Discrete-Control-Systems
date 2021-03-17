from RandomNumberGenerator import RandomNumberGenerator
from Calculate import calculate


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
        qj.append(generator.nextInt(1,29))

    #wypisanie zadań i kolejnych czasow zadań
    print("nr:", nr)
    print("rj: ", rj)
    print("pj: ", pj)
    print("qj: ", qj)
    print("\n")

    Cmax = calculate(rj, pj, qj, maxTaskNumber)
    
if __name__ == '__main__':
	main()