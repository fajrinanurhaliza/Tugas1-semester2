uang_awal = int(input('Masukkan Uang Awal : '))
tanggal = str(input('Masukkan Tanggal : '))
jumlah_pengeluaran = int(input('Masukkan Jumlah Pengeluaran : '))

uang_sisa = uang_awal-jumlah_pengeluaran 
if uang_sisa >= 100000:
    print(tanggal,'Uangmu masih banyak','sisa uang',uang_sisa)
else:
    print(tanggal,'Uangmu sisa dikit, berhematlah!!','sisa uang',uang_sisa)