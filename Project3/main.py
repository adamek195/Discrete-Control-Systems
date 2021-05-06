from RandomNumberGenerator import RandomNumberGenerator
from greedy_algorithm import greedy
from calculate import target_fun
from brute_force import brute_force


def main():
    seed = int(input("Wprowadź Z: "))
    generator = RandomNumberGenerator(seed)
    taskNumber = int(input("Wprowadź rozmiar problemu: "))
    tasks = range(1, taskNumber+1)
    nr=[]
    pj=[] #czas wykonania
    wj=[] #waga/współczynnik kary
    dj=[] #żądany termin zakończenia

    for task in tasks:
        nr.append(task)
        pj.append(generator.nextInt(1,29))

    A = 0
    for number in pj:
        A += number

    for task in tasks:
        wj.append(generator.nextInt(1,9))
    X = 29
    #X=A
    for task in tasks:
        dj.append(generator.nextInt(1,X))

    print("Poczatkowe ustawienie\n")
    print("\nnr:", nr)
    print("pj: ", pj)
    print("wj ", wj)
    print("dj", dj)
    print("\n")

    print(f'WiTi dla początkowego = {target_fun(pj,wj,dj,taskNumber)}')
    print(f'WiTi dla Brute Force = {brute_force(pj,wj,dj,taskNumber)}')
    print(f'WiTi dla Greedy algorithm = {greedy(pj,wj,dj,taskNumber)}')

if __name__ == '__main__':
	main()
