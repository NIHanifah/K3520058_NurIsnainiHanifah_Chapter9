nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' :  80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' :  90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("===============================================================================")
print("NIM".ljust(10),  "NAMA".ljust(14), "N.MID".ljust(13), "N.UAS".ljust(15), "N.AKHIR".ljust(15), "STATUS".ljust(15))
print("-------------------------------------------------------------------------------")
i = 0
while i < len(nilai):
    nilaiAkhir = round((nilai[i]['mid'] + 2 * nilai[i]['uas']) / 3, 1)
    if nilaiAkhir >= 60:
        print(nilai[i]['nim'].ljust(10), nilai[i]['nama'].ljust(15), nilai[i]['mid'], "".rjust(10), nilai[i]['uas'], "".rjust(10), nilaiAkhir, "LULUS".rjust(15))
    elif nilaiAkhir < 60:
        print(nilai[i]['nim'].ljust(10), nilai[i]['nama'].ljust(15), nilai[i]['mid'], "".rjust(10), nilai[i]['uas'], nilaiAkhir.rjust(10), "TIDAK LULUS")
    i += 1
print("-------------------------------------------------------------------------------")