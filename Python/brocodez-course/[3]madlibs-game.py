#ini adalah program game madlibs, cara kerjanya adalah user menginput variable variable yang ada tanpa mengetahui kalimatnya seperti apa, setelah user menginput semua variable, maka ussr akan mendapatkan sebuah output yang merupakan cerita yang subjek, objek, kata sifat, kata kerja yang diacak
tempat = input("Input nama tempat/orang: ")
subjek = input("Input nama orang/hewan: ")
kata_sifat1 = input("Input kata sifat: ")
kata_sifat2 = input("Input kata sifat: ")
kata_sifat3 = input("Input kata sifat: ")
kata_kerja = input("Input kata kerja: ")

print(f"""
Aku sedang pergi ke {tempat} yang {kata_sifat1},
Dijalan, Aku melihat {subjek} yang sedang {kata_kerja},
{subjek} terlihat sangat {kata_sifat2},
Aku pun pulang kerumah dengan sangat {kata_sifat3}
""")
