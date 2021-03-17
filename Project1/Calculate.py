from typing import List

#liczenie wartości funkcji celu
def calculate(rj : List[int], pj: List[int], qj: List[int],taskNumber):
    #wektor rozpoczecia kolejnych zadan
    Sj = []
    #wektor momentow zakończenia zadan
    Cj = []
    #wektor kolejnych optymalnych zakończeń zadań
    Cmaxj = []
    #inicjalizacja pierwszych argumentow wektorów gdzie C_0 = 0
    Sj.append(max(rj[0],0))
    Cj.append(Sj[0]+pj[0])
    Cmaxj.append(Cj[0] + qj[0])
    Cmax = Cmaxj[0]
    #przypisanie kolejncyh argumentów
    for j in range(1, taskNumber):
        Sj.append(max(rj[0], Cj[j-1]))
        Cj.append(Sj[j]+ pj[j])
        Cmaxj.append(Cj[j] + qj[j])
        Cmax = max(Cmax, Cmaxj[j])
    return Cmax
