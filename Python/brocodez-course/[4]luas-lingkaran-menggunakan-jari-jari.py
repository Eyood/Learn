#ini adalah program untuk menghitung sebuah lingkaran menggunakan jari jari
import math #menginport math module
jari_jari = float(input("Masukkan panjang jari jari dari sebuah lingkaran: ")) #mengambil variable jari jari sebuah lingkaran dari user
luas_lingkaran = math.pi * math.pow(jari_jari, 2) #menghitung luas lingkaran menggunakan pi dikali jari jari pangkat dua, math.pi sama dengan pi dengan 15 akurat digit pi dibelakang desimal, math.pow sama aja kaya jari_jari**2
print(f"Luas lingkaran dengan jari jari {jari_jari} adalah {luas_lingkaran}") #memberikan output luas lingkaran kepada user