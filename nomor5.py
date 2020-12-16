#menampilkan suatu data

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' :  80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' :  90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("============================================")
print("NIM".ljust(10),  "NAMA".ljust(14), "N.MID".ljust(13), "N.UAS")
print("--------------------------------------------")
i = 0
while i < len(nilai):
    print(nilai[i]['nim'].ljust(10), nilai[i]['nama'].ljust(15), nilai[i]['mid'], "".rjust(10), nilai[i]['uas'], )
    i += 1
print("--------------------------------------------")