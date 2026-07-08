#ini adalah program simulasi belanja
barang = input("Barang apa yang ingin anda beli?: ") #mengambil variable barang yang akan dibeli oleh user
jumlah = float(input(f"Berapa banyak Anda ingin membeli {barang}?: ")) #mengambil variable jumlah barang yang akan dibeli oleh user
harga = float(input("Berapa harga barang tersebut?: Rp.")) #mengambil variable harga barang yang akan dibeli oleh user
total = jumlah * harga #menghitung total pembayaran yang harus dilakukan user dengan mengkalikan variable jumlah dan variable harga
print(f"Terimakasih sudah berbelanja, anda membeli {jumlah} {barang} dengan harga satuannya adalah {harga}, jadi total yang harus anda bayar adalah Rp.{total}0") #memberikan output kepada user yang berisi kata kata dari penjual, jumlah barang yang dibeli, barang yang dibeli, harga barang yang dibeli, dan total harga yang harus dibayar