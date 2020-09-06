

f = open("rosalind_gc.txt","r")  
lista = ''.join([x.strip('\r\n') for x in f.readlines()]).split('>Rosalind_')
f.close()
dictio = {}
del lista[0]
for char in lista:
    cntcg = 0;
    cnt=0;
    stringa = str(char[4:])
    for c in stringa:
        cnt +=1
        if c =='C' or c=='G':
            cntcg+=1
    dictio[char[:4]]=(100.000*cntcg)/cnt
maxi = max(dictio, key=dictio.get)
print(">Rosalind_"+str(maxi)+'\n'+("{0:.6f}".format(round(dictio[maxi],6))))