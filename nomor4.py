#mengacak huruf pada kata
#menggunakan shuffle

import random
import collections

#membuat susunan huruf yang berbeda 

def shuffleString(x, n):
    kata = list(x)
    listKata = []
    k = 0
    while k < n:
        random.shuffle(kata)
        hasil = ''.join(kata)
        if hasil not in listKata:
            listKata.append(hasil)
            k += 1
    print(listKata)
shuffleString('aku', 3)