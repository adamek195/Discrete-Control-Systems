import math

#definicja klasy generujaca liczby
class RandomNumberGenerator:
    def __init__(self, seedVaule=None):
        self.__seed=seedVaule
    def nextInt(self, low, high):
        m = 2147483647
        a = 16807
        b = 127773
        c = 2836
        k = int(self.__seed / b)
        self.__seed = a * (self.__seed % b) - k * c
        if self.__seed < 0:
            self.__seed = self.__seed + m
        value_0_1 = self.__seed
        value_0_1 =  value_0_1/m
        return low + int(math.floor(value_0_1 * (high - low + 1)))
    def nextFloat(self, low, high):
        low*=100000
        high*=100000
        val = self.nextInt(low,high)/100000.0
        return val

#funkcja sortujaca
def sortKey(e):
    return e[1]

def main(): 
    #pobieramy ziarno Z
    seed = int(input("Wprowadź Z:"))
    #dla podanego ziarna wywolujemy konstruktor parametryczny
    generator = RandomNumberGenerator(seed) 
    #wprowadzamy liczbe zadan n
    maxTaskNumber = int(input("Wprtowadź liczbe zadań:"))
    #inicjalizacja listy zadan
    tasks = range(1, maxTaskNumber+1)
    #kolejnośc wykonywania zadań na maszynie
    pi = [] 
    #czas przygotowania kolejnych zadań
    rj = [] 
    #czas wykonania kolejnych zadan
    pj = [] 

    #dla pobranych ilości zadań n losujemy czas wykonania kolejnych zadań
    for task in tasks:   
        pi.append(task)
        pj.append(generator.nextInt(1,29))

    #suma kolejnych czasow wykonania zadan
    sumA = 0
    for number in pj:
        sumA += number

    #dla pobranych ilosci zadan przypisujemy kolejne czasy wykonania poszczególnych zadań
    for task in tasks:
        rj.append(generator.nextInt(1,sumA))

    #wypisanie zadań i kolejnych czasow zadań
    print("nr:", pi)
    print("rj: ", rj)
    print("pj: ", pj)
    print("\n")

    #wektor rozpoczęcia wykonywania zadań
    Sj = []
    #wektor zakończenia zadań
    Cj = []  

    #inicjalizacja pierwszych argumentow wektorów gdzie C_0 = 0
    Sj.append(max(rj[0],0))
    Cj.append(Sj[0]+pj[0])

    #przypisanie kolejncyh argumentów
    for task in tasks[:-1]:
        Sj.append(max(rj[task],Cj[task-1]))
        Cj.append(Sj[task]+pj[task])

    #wypisanie wektorow po czasie
    print("Sj:",Sj)
    print("Cj: ",Cj)
    print("\n")

    #sortowanie wektorow
    solution = []
    for task in tasks: 
        solution.append([pi[task-1],rj[task-1],pj[task-1]])   

    #sorotwanie zadań
    solution.sort(key=sortKey)

    #posortowane numery zadań
    PiSolution = []
    #posortowany wektor rozpoczęcia kolejnych zadań
    SjSolution = []
    #posortowany wektor zakonczenia kolejncych zadań
    CjSolution = []

    #dodanie posortowanych zadań
    for task in tasks:
        PiSolution.append(solution[task-1][0])

    #inicjalizacja pierwszych posortowanych argumentow wektorów gdzie C_0 = 0
    SjSolution.append(max(solution[0][1],0))
    CjSolution.append(SjSolution[0]+solution[0][2])

    #przypisanie kolejncyh posortowanych argumentów
    for task in tasks[:-1]:
        SjSolution.append(max(solution[task][1], CjSolution[task-1]))
        CjSolution.append(SjSolution[task]+solution[task][2])
       
    #wypisanie posorotwanych wektorow
    print("Sorted tasks:")
    print("pi:", PiSolution)
    print("Sj:",SjSolution)
    print("Cj: ",CjSolution)



if __name__ == '__main__':
	main()