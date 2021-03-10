import math

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

def sortKey(e):
    return e[1]

def main(): 
    seed = int(input("Wprowadź Z:"))
    generator = RandomNumberGenerator(seed) #konstruktor 
    maxTaskNumber = int(input("Wprtowadź liczbe zadań:"))
    tasks = range(1, maxTaskNumber+1)
    pi = [] #kolejnośc wykonywania zadań
    rj = [] #czas przygotowania
    pj = [] #czas wykonaina 
    for task in tasks:   
        pi.append(task)
        pj.append(generator.nextInt(1,29))

    sumA = 0
    for number in pj:
        sumA += number

    for task in tasks:
        rj.append(generator.nextInt(1,sumA))

    print("rj: ", rj)
    print("pj: ", pj)

    Sj = [] #moment rozpoczęcia wykonywania zadania 
    Cj = [] #moment zakończenia zadania 
    Sj.append(max(rj[0],0))
    Cj.append(Sj[0]+pj[0])

    for task in tasks[:-1]:
        Sj.append(max(rj[task],Cj[task-1]))
        Cj.append(Sj[task]+pj[task])

    print("Sj:",Sj)
    print("Cj: ",Cj)

    solution = []
    for task in tasks: 
        solution.append([pi[task-1],rj[task-1],pj[task-1]])

    solution.sort(key=sortKey)

    SjSolution = []
    CjSolution = []

    SjSolution.append(max(solution[0][1],0))
    CjSolution.append(SjSolution[0]+solution[0][2])

    for task in tasks[:-1]:
        SjSolution.append(max(solution[task][1], CjSolution[task-1]))
        CjSolution.append(SjSolution[task]+solution[task][2])
       

    print("Solution:")
    print("Sj:",SjSolution)
    print("Cj: ",CjSolution)



if __name__ == '__main__':
	main()