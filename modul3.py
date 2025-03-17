print ("\n========SELAMAT DATANG PADA PERMAINAN ANGKA BOM!!========")
print("\n")
Pemain_1 = str(input("Masukkan nama pemain 1 : "))
Pemain_2 = str(input("Masukkan nama pemain 2 : "))

print("\n====================PERMAINAN DIMULAI====================")
print (f"\n{Pemain_1} silahkan tentukan")
n = int(input("Batas angka positif : "))
k = int(input("Angka BOM           : "))

for i in range (1,n+1) :
    if i%k == 0 :
        print ("BOM", end= " ")
    else :
        print (i, end= " ")

print("\n")
print("========================================================")
print (f"\n{Pemain_2} silahkan tebak angka dari 1 sampai {n}")

while True :
    Tebak_angka = int(input("Tebak angka : "))
    if 1 <= Tebak_angka <= n :
        break
    print ("Angka yang anda masukkan tidak valid, coba lagi")
    
if Tebak_angka%k == 0 :
    print(f"{Tebak_angka} adalah angka BOM, yah {Pemain_2} kalah")
else :
    print(f"{Tebak_angka} bukan angka BOM, selamat {Pemain_2} menang")

print("\n====================PERMAINAN SELESAI====================")