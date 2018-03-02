from operator import itemgetter

R=0
C=0
F=0
W=0
B=0
T=0
t=0 # contatore tempo
taxi = []
lista = []

def distanza(a,b,x,y):
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

    #Ride contiene [x,y  a,b  s,f  posizione]
    global R,C,F,W,B,T
    R=PrimaRiga[0]
    C=PrimaRiga[1]
    F=PrimaRiga[2]
    W=PrimaRiga[3]
    B=PrimaRiga[4]
    T=PrimaRiga[5]
    for i in range(F):
       taxi.append([0,0,0,"",0]) # x-ora, y-ora, dist-percorsa stringa da stampare e numero di ride
    return richieste



def calcolaPunteggio(ride,x,y,t):# xy = dove sono ora
    dist = distanza(x,y,ride[0],ride[1]) #distanza per arrivare partenza
    tragitto = distanza(ride[0],ride[1],ride[2],ride[3]) #distanza da partenza ad arrivo
    if dist+t+tragitto>ride[5] or dist+t+tragitto>T:
        return -800000
    if t+dist+tragitto<=ride[4]:
        b=B
    else:
        b=0
    return tragitto+b-dist*0.5


def funzione(taxi,richieste):
    for vett in taxi:
        if len(richieste) == 0:
            return
        max=0
        indice= 0
        i=0
        for i in range(len(richieste)):
            temp = calcolaPunteggio(richieste[i],vett[0],vett[1],vett[2])
            if temp>max:
                max = temp
                indice = i

        vett[3] = vett[3]+" "+str(richieste[indice][6])
        #print(richieste[indice])
        vett[2] = vett[2]+distanza(vett[0],vett[1],richieste[indice][2],richieste[indice][3])
        vett[0] = richieste[indice][2]
        vett[1] = richieste[indice][3]
        vett[4] += 1
        del richieste[indice]
        if len(richieste) == 0:
            return




if __name__ == '__main__':

    input="/home/andrea/Scrivania/Hash_Code_2018/d.in"
    output="/home/andrea/Scrivania/Hash_Code_2018/d.out"
    richieste = leggiStrada(input)
    for i in range(1000000000000):
        funzione(taxi,richieste)

    fout = open(output,"w")
    fout.close()
    fout = open(output, "a")
    for vett in taxi:
        fout.write(str(vett[4])+vett[3]+"\n")
    fout.close