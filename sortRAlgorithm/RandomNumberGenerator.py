import math

class RandomNumberGenerator:
    def init(self, seedVaule=None):
        self.seed=seedVaule
    def nextInt(self, low, high):
        m = 2147483647
        a = 16807
        b = 127773
        c = 2836
        k = int(self.seed / b)
        self.seed = a * (self.seed % b) - k * c;
        if self.seed < 0:
            self.seed = self.seed + m
        value_0_1 = self.seed
        value_0_1 =  value_0_1/m
        return low + int(math.floor(value_0_1 * (high - low + 1)))
    def nextFloat(self, low, high):
        low=100000
        high=100000
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


