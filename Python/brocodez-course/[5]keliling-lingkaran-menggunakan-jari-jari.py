#ini adalah program untuk menghitung keliling lingkaran menggjnakan jari jari
import math #mengimport math module
jari-jari = float(input("Masukkan jadi jari jari sebuah lingkaran: ")) #mengambil variable jari jari dari user lalu mengubahnya menjadi tipe float
keliling_lingkaran = 2 * math.pi * jari-jari #membuat variable keliling lingkaran dengan cara mengkalikan 2 dengan pi lalu dikali jari jari yang user input tadi
print(f"Keliling lingkaran yang memiliki jari jari {jari-jari} adalah {keliling_lingkaran}") #memberikan output keliling lingkaran kepada user