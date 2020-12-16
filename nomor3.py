#membuah bintang atas bawah
#dengan perintah center()

def bintang(n):
    k = 1
    while 0 < n:
        while 4 <= n:
            j = "*" * (k)
            print(j.center(15))
            n -= 1
            k += 2
        while n < 4:
            j = "*" * ((n-1)*2 + 1)
            print(j.center(15))
            n -= 1
            break

bintang(7)
