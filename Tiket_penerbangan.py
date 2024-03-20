Tiket=str(input('===============TIKET PENERBANGAN==============='))
Nama =str(input('Nama          :'))
Umur =int(input('Umur          :'))
Jenis_Kelamin =str(input('Jenis Kelamin :'))
print()
print('Kota Tujuan ')
print('1.Padang')
print('2.Medan')
print('3.Jakarta')
Kota_Tujuan =str(input('Pilih Kota Tujuan(Padang/Medan/Jakarta) :'))
print()
print('Jenis Kelas ')
print('1.Ekonomi,harga:750000')
print('2.Bisnis,harga:1500000')
print('3.First ,harga:3000000')
Jenis_Kelas =str(input('Pilih Jenis Kelas(Ekonomi/Bisnis/First) :'))
print()
if Jenis_Kelas == 'Ekonomi': 
   harga = 750000
elif Jenis_Kelas == 'Bisnis' :
   harga = 1500000
else :
   harga = 3000000
   
jumlah_kursi =int(input('Jumlah Kursi :'))
total_harga=harga*jumlah_kursi
if jumlah_kursi > 3:
   total_harga =total_harga*0.75
print()
print('===============TIKET PENERBANGAN===============')   
print('Nama          :'+Nama)
print('Umur          :'+str(Umur))
print('Jenis Kelamin :'+Jenis_Kelamin)
print('Kota Tujuan   :'+Kota_Tujuan)
print('Jenis Kelas   :'+Jenis_Kelas)
print('Jumlah Kursi  :'+str(jumlah_kursi))
print('Harga         :'+str(total_harga))

    