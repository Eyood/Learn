#ini adalah program untuk mengkonversi satuan jarak mm, cm, inch, foot, yard, m, km, mile

#kpk dari ya gitulah, buat mempermudah gw konversi aja
mm = 4057348608000

konversi = {
  "mm" : 4057348608000,
  "cm" : mm / 10,
  "inch" : mm / 25.4,
  "foot" : mm / 304.8,
  "yard" : mm / 914.4,
  "m" : mm / 1000,
  "km" : mm / 1000000,
  "mile" : mm / 1609344,
}
#mengambil input user
print("Konversi Satuan A ke satuan B")
panjang1 = float(input("Masukkan Panjang A:"))
print("(mm/cm/inch/foot/yard/m/km/mile)")
satuan1 = input("Masukkan Satuan A: ")
if satuan1 not in konversi:
  print(f"satuan {satuan1} tidak ada di list")
  exit()
satuan2 = input("Masukkan Satuan B: ")
if satuan2 not in konversi:
  print(f"satuan {satuan2} tidak ada di list")
  exit()
  
#program konversi  
panjang2 = panjang1 * konversi[satuan2]/konversi[satuan1]
print(panjang2)