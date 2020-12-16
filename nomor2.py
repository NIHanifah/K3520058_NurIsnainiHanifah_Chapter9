#membuat bintang dengan perintah center()

def bintang(n):
    k = 1
    while 0 < n:
        j = "*" * (k)
        print(j.center(9))
        n -= 1
        k += 2
bintang(4)