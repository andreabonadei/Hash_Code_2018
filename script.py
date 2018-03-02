# coding=utf-8
from operator import itemgetter

R=0     #Num righe
C=0     #Num colonne
F=0     #Num taxi
W=0     #
B=0     #Bonus
T=0     #Numero massimo di step (max distanza percorsa per taxi
taxi = [] # [x,y,  dist_percorda, stringa da stampare, numero di ride effettuate]
lista = []

def distanza(a,b,x,y):  #Calcola la distanza tra due punti
    if (a-x)<0:
        A=-(a-x)
    else:
        A=a-x
    if (b-y)<0:
        B=-(b-y)
    else:
        B=b-y

    return A+B

def leggiStrada(nomeFile):
    fin = open(nomeFile,"r")
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
        ride.append(i)
        richieste.append(ride)

    global R,C,F,W,B,T
    R=PrimaRiga[0]
    C=PrimaRiga[1]
    F=PrimaRiga[2]
    W=PrimaRiga[3]
    B=PrimaRiga[4]
    T=PrimaRiga[5]
    for i in range(F):
       taxi.append([0,0,0,"",0])
    return richieste



def calcolaPunteggio(ride,x,y,t):# (x,y) = dove sono ora, t è la distanza percorsa dal taxi fino ad ora (tempo trascorso)
    dist = distanza(x,y,ride[0],ride[1]) #distanza per arrivare al punto di partenza
    tragitto = distanza(ride[0],ride[1],ride[2],ride[3]) #distanza da partenza ad arrivo
    if dist+t+tragitto>ride[5] or dist+t+tragitto>T:
        return -8000000000
    if t+dist+tragitto<=ride[4]:
        b=B
    else:
        b=0
    return tragitto+b-dist*0.3

# Scartiamo sempre le ride più brevi perchè hanno un punteggio basso (RISOLVERE)
#Con tragitto+b-dist*0.5 punteggio massimo per il file C
#

def funzione(taxi,richieste):
    for vett in taxi:
        if len(richieste) == 0:
            return -1
        max=-800000099999
        indice= 0
        i=0
        for i in range(len(richieste)):         #Cerco la richiesta con punteggio più alto per il taxi attuale
            temp = calcolaPunteggio(richieste[i],vett[0],vett[1],vett[2])
            if temp>max:
                max = temp
                indice = i

        # Aggiungo alla stringa la ride effettuata
        vett[3] = vett[3]+" "+str(richieste[indice][6])

        # Aggiorno la distanza percorsa dal taxi
        vett[2] = vett[2]+distanza(vett[0],vett[1],richieste[indice][2],richieste[indice][3])

        # Assegno al taxi la posizione attuale (al termine della ride)
        vett[0] = richieste[indice][2]
        vett[1] = richieste[indice][3]

        #Aumento il contatore delle ride effettuate
        vett[4] += 1

        #Elimino la ride effettuata dalle richieste
        del richieste[indice]
        if len(richieste) == 0:
            return -1       #Finito le richieste

    return 0




if __name__ == '__main__':


    for i in ('a','b','c','d','e'):

        input = i+ ".in"
        output = i+ ".out"
        print ("Input file ---> %s.in" % i)
        richieste = leggiStrada(input)
        conta=0
        while(funzione(taxi,richieste)!=-1):
            conta+=1
            print("Computing %d ...." % conta)

        #Creo un file pulito
        fout = open(output,"w")
        fout.close()

        #Scrivo sul file le ride effettuate
        fout = open(output, "a")
        for vett in taxi:
            fout.write(str(vett[4])+vett[3]+"\n")
        fout.close