import random
import sys
R = C = F = W = B = T = 0
taxi = []
lista = []
richieste = []
richiesteUsate = []


def distanza(a, b, x, y):
    if (a-x) < 0:
        A = -(a-x)
    else:
        A = a-x
    if (b-y) < 0:
        B = -(b-y)
    else:
        B = b-y
    return A+B


def leggiStrada(nomeFile):
    fin = open(nomeFile, "r")
    riga = fin.readline().split()
    #richieste = []
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
        ride.append(i)
        ride.append(False) # ride usata?
        richieste.append(ride)

    # Ride contiene [x,y  a,b  s,f  posizione, usata?]
    global R, C, F, W, B, T
    R = PrimaRiga[0]
    C = PrimaRiga[1]
    F = PrimaRiga[2]
    W = PrimaRiga[3]
    B = PrimaRiga[4]
    T = PrimaRiga[5]
    for i in range(F):
        taxi.append([0, 0, 0, "", 0, False, -1])
        # taxi.append([0, 0, 0, "", 0])  # x-ora, y-ora, dist-percorsa, stringa da stampare e numero di ride
    #return richieste


def calcolaPunteggio(ride, x, y, time):  # xy = dove sono ora
    dist = distanza(x, y, ride[0], ride[1])  # distanza per arrivare partenza
    tragitto = distanza(ride[0], ride[1], ride[2], ride[3])  # distanza da partenza ad arrivo
    if dist+time+tragitto >= ride[5] or dist+time+tragitto > T:
        return -8000000000
    if time+dist <= ride[4]:
        b = B
    else:
        b = 0
    c = T-dist-tragitto-time-ride[5]
    # c = T-ride[5]-t-dist*0.3-tragitto
    #return tragitto+b+c-dist - calcolaTempoPercorso(ride)
    return tragitto+b+c + calcolaTempoPercorso(ride)

"""Scartiamo sempre le ride più brevi perchè hanno un punteggio basso
    Con tragitto+b-dist*0.5 punteggio massimo per il file C"""


def funzione(taxi, richieste):
    for vett in taxi:
        if len(richieste) == 0:
            return -1
        max = -800000000
        indice = 0
        i=0
        for i in range(len(richieste)):
            temp = calcolaPunteggio(richieste[i], vett[0], vett[1], vett[2])
            if temp > max:
                max = temp
                indice = i

        vett[3] = vett[3]+" "+str(richieste[indice][6])
        vett[2] = vett[2]+distanza(vett[0], vett[1], richieste[indice][2], richieste[indice][3])
        vett[0] = richieste[indice][2]
        vett[1] = richieste[indice][3]
        vett[4] += 1
        del richieste[indice]
        if len(richieste) == 0:
            return -1
    return 0


"""if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])
    input = sys.argv[1]
    output = sys.argv[2]
#   input = "/home/viga/Scrivania/Hash_Code_2018/d.in"
#   output = "/home/viga/Scrivania/Hash_Code_2018/d.out"
    richieste = leggiStrada(input)
    conta=0
    while funzione(taxi, richieste) != -1:
        conta += 1
        print("Computing %d ...." % conta)
    fout = open(output, "w")
    fout.close()
    fout = open(output, "a")
    for vett in taxi:
        fout.write(str(vett[4])+vett[3]+"\n")
    fout.close"""


def funzione2():
    """taxi.append([0, 0, 0, "", 0, False, -1])
    x-ora, y-ora, dist-percorsa,
    stringa da stampare, numero di ride fatte, isOccupata, quale ride sta facendo"""
    # Ride contiene [x,y  a,b  s,f  posizione, usata]
    time = 0
    flag = False
    while time <= T:
        for vett in taxi:
            if vett[5]:
                muovi(vett)
                vett[2] += 1
                if isArrivata(vett):
                    vett[5] = False
                    vett[6] = -1
                continue
            if len(richieste) == 0:
                return
            max = -800000000
            indice = 0
            for i in range(len(richieste)):
                if richieste[i][7]:
                    continue
                #  temp = calcolaPunteggio(richieste[i], vett[0], vett[1], vett[2])
                temp = calcolaPunteggio(richieste[i], vett[0], vett[1], time)
                if temp > max:
                    max = temp
                    indice = i

            if richieste[indice][6] == 0:
                if not flag:
                    vett[5] = True
                    vett[3] = vett[3] + " " + str(richieste[indice][6])
                    vett[4] += 1
                    vett[6] = indice
                    richieste[indice][7] = True
                    flag = True
                continue

            vett[5] = True
            vett[3] = vett[3] + " " + str(richieste[indice][6])
            vett[4] += 1
            richiesteUsate.append(richieste[indice])
            vett[6] = richiesteUsate.index(richieste[indice])
            #richieste[indice][7] = True
            del richieste[indice]
        if time % 10000 == 0:
            print("Istante %d" % time, len(richieste))
        #print(richieste)
        time += 1


def isArrivata(vett):
    ride = richiesteUsate[vett[6]]
    return ride[2] == vett[0] and ride[3] == vett[1]


def muovi(vett):  # prima mi muovo in orizzontale e poi in verticale
    ride = richiesteUsate[vett[6]]
    if ride[3] > vett[1]:
        vett[1] += 1
    elif ride[3] < vett[1]:
        vett[1] -= 1
    elif ride[2] < vett[0]:
        vett[0] -= 1
    elif ride[2] > vett[0]:
        vett[0] += 1
    vett[2] += 1


def calcolaTempoPercorso(ride):
    return ride[5] - ride[4]


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])
    input = sys.argv[1]
    output = sys.argv[2]
#   input = "/home/viga/Scrivania/Hash_Code_2018/d.in"
#   output = "/home/viga/Scrivania/Hash_Code_2018/d.out"
    leggiStrada(input)
    funzione2()
    fout = open(output, "w")
    for vett in taxi:
        fout.write(str(vett[4])+vett[3]+"\n")
    fout.close()