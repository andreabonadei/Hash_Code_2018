import numpy as np
R=0
C=0
F=0
W=0
B=0
T=0

def leggiStrada(nomeFile):
    fin = open(nomeFile)
    riga = fin.readline().split()
    richieste = []
    PrimaRiga = []
    for i in range(len(riga)):
        n = int(riga[i])
        PrimaRiga.append(n)
    for i in range(PrimaRiga[3]):
        ride = []
        riga = fin.readline().split()
        for j in range(len(riga)):
            n = int(riga[j])
            ride.append(n)
        richieste.append(ride)
    R=PrimaRiga[0]
    C=PrimaRiga[1]
    F=PrimaRiga[2]
    W=PrimaRiga[3]
    B=PrimaRiga[4]
    T=PrimaRiga[5]
    return richieste

if __name__ == '__main__':
    richieste = leggiStrada("/home/viga/PycharmProjects/HashCode/a_example.in")
    print(richieste)