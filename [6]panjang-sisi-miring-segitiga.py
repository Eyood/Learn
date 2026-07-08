#ini adalah program untuk menghitung panjang sisi miring atau sisi c dari sebuah segitiga menggunakan panjang sisi a dan sisi b
import math #mengimport math module
panjang_sisi_a = float(input("Panjang sisi A segitiga: ")) #mengambil variable panjang sisi a segitiga dari user
panjang_sisi_b = float(input("Panjang sisi B segitiga: ")) #mengambil variable panjang sisi b segitiga dari user
panjang_sisi_c = math.sqrt(pow(panjang_sisi_a, 2) + pow(panjang_sisi_b, 2)) #membuat variable panjang sisi c dari sebuah segitiga menggunakan rumus akar a kuadrat ditambah b kuadrat
print(f"Panjang sisi c dari segitiga yang panjang sisi a nya {panjang_sisi_a} dan panjang sis b nya {panjang_sisi_b} adalah {panjang_sisi_c}") #memberikan output panjang sisi c segitiga yang sudah di hitung kepada user