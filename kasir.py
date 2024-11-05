print("==============Warung Amanah============")
Pembeli = input("Nama Pembeli : ")

totalmakanan = 0
totalminuman = 0

def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n==============MENU MAKANAN=====================")
    print("1. Nasi Ayam Mentega - Rp.25000,00")
    print("2. Nasi Goreng Seafood - Rp.30000,00")
    print("3. Mie Goreng Baso - Rp.20000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3 : "))
    porsi = int(input("Berapa Porsi : "))
    
    if nomor == 1:
        totalmakanan = porsi * 25000
        print(porsi,' Nasi Ayam Mentega = Rp.',totalmakanan)
        makan = "Nasi Ayam Mentega"
    elif nomor == 2:
        totalmakanan = porsi * 30000
        print(porsi,'Nasi Goreng Seafood = Rp.',totalmakanan)
        makan = "Nasi Goreng Seafood"
    elif nomor == 3:
        totalmakanan = porsi * 20000
        print(porsi,' Mie Goreng Baso = Rp.',totalmakanan)
        makan = "Mie Goreng Baso"
    else:
        print("Pilihan tidak ada dalam daftar menu\nSilahkan pilih kembali !!!")

def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n==============MENU MINUMAN=====================")
    print("1. Es Teh - Rp.10000,00")
    print("2. Milk Shake Stawberry - Rp.25000,00")
    print("3. Jus Mangga - Rp.20000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3 : "))
    gelas = int(input("Berapa gelas : "))
    
    if nomor == 1:
        totalminuman = gelas * 10000
        print(gelas,' Es Teh = Rp.',totalminuman)
        minum = "Es Teh"
    elif nomor == 2:
        totalminuman = gelas * 25000
        print(gelas,'Milk shake Stawberry = Rp.',totalminuman)
        minum = "Milk Shake Stawberry"
    elif nomor == 3:
        totalminuman = gelas * 20000
        print(gelas,' Jus Mangga = Rp.',totalminuman)
        minum = "Jus Mangga"
    else:
        print("Pilihan tidak ada dalam daftar menu\nSilahkan pilih kembali !!!")

makanan()
minuman()

total_semua = totalmakanan + totalminuman

print("\nTotal yang harus di bayar : ",total_semua)
uang = int(input("Uang Tunai Pembeli : Rp."))
kembalian = uang - total_semua

print("\n==============Struk Pembelian==============")
print("Nama\t\t:", Pembeli)
print("Beli\t\t:", porsi, makan, "(Rp.", totalmakanan, ")")
print("\t\t:", gelas, minum, "(Rp.", totalminuman, ")")
print("Tagihan\t\t:Rp.", total_semua)
print("Dibayar\t\t: Rp.", uang)
print("Kembalian\t: Rp.", kembalian)

print("==============================")
print("==============================")