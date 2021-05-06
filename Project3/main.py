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

    print("\nnr:", nr)
    print("pj: ", pj)
    print("wj ", wj)
    print("dj", dj)

    witi_start = target_fun(pj,wj,dj,taskNumber)
    print(f'\nWiTi dla początkowego = {witi_start[0]}')
    print(f'C: {witi_start[2]}')
    print(f'T: {witi_start[1]}')


    witi_greedy = greedy(pj,wj,dj,taskNumber)
    print(f'\nWiTi dla Greedy algorithm = {witi_greedy[0]}')
    print(f'C: {witi_greedy[2]}')
    print(f'T: {witi_greedy[1]}')

    witi_brute_force = brute_force(pj,wj,dj,taskNumber)
    print(f'\nWiTi dla Brute Force = {witi_brute_force[0]}')
    print(f'C: {witi_brute_force[2]}')
    print(f'T: {witi_brute_force[1]}')

if __name__ == '__main__':
	main()
