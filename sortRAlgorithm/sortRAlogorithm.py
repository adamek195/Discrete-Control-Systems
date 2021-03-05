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
        self.__seed = a * (self.__seed % b) - k * c;
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

def main(): 
    seed = int(input("Wprowadź Z:"))
    generator = RandomNumberGenerator(seed) #konstruktor 
    maxTaskNumber = int(input("Wprtowadź liczbe zadań:"))
    tasks = range(1, maxTaskNumber+1)
    rj = []
    pj = []
    for task in tasks:   
        pj.append(generator.nextInt(1,29))

    sumA = 0
    for number in pj:
        sumA += number

    for task in tasks:
        rj.append(generator.nextInt(1,sumA))


    print("rj: ", rj)
    print("pj: ", pj)

if __name__ == '__main__':
	main()