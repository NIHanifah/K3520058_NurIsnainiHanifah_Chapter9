#mengubah huruf pada kata
#menggunakan replace

def ubahHuruf(kata, a, b):
    kata = "".join(list(kata.replace(a,b)))
    print(kata)

ubahHuruf('MATEMATIKA', 'T', 'S')