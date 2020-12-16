#membuat list data

mhs = ['K001:ROSIHAN ARI        :1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN        :2005-01-28:KARANGANYAR']
print("==========================================================================")
print("NIM".ljust(10), "NAMA MAHASISWA".ljust(25), "TGL LAHIR".ljust(20), "TEMPAT LAHIR")
print("--------------------------------------------------------------------------")

i = 0
while i<len(mhs):
       dataBaru = mhs[i].split(':')
       tanggalBaru = dataBaru[2].split('-')
       print(dataBaru[0].ljust(8), dataBaru[1].ljust(15), tanggalBaru[2].rjust(10),"/", tanggalBaru[1], "/", tanggalBaru[0].ljust(10), dataBaru[3])
       i += 1
print("--------------------------------------------------------------------------")