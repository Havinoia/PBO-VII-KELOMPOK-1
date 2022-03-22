#TUGAS KELOMPOK 1
#5210411215 WILLIAM KESSLER SURdANTO
#5210411212 HAVIN NEO DIMAS NUGRAHA
#5210411232 M. TAUFIK NAMAWI
#5210411247 REVI ANANDA KIRANA PUTRI

class Kalkulator :
    def __init__(self, c, d) :
        self.a = c
        self.b = d  
#KELOMPOK 1
class Tambah(Kalkulator) :
    def __init__(self, c, d):
        super().__init__(c, d)

    def tambah(self) :
        print("Hasil penjumlahan adalah ")
        self.hasil = self.a + self.b    
        print(f"{c} + {d} = {self.hasil}")
        print("------------------------------------")

class Kurang(Kalkulator) :
    def __init__(self, c, d):
        super().__init__(c, d)

    def kurang(self) :
        print("Hasil pengurangan adalah")
        self.hasil = self.a - self.b
        print(f"{c} - {d} = {self.hasil}")  
        print("------------------------------------")
#KELOMPOK 1
class Kali(Kalkulator) :
    def __init__(self, c, d):
        super().__init__(c, d)

    def kali(self) :
        print("Hasil perkalian adalah ")
        self.hasil = self.a * self.b    
        print(f"{c} * {d} = {self.hasil}")
        print("------------------------------------")
        

class Bagi(Kalkulator) :
    def __init__(self, c, d):
        super().__init__(c, d)

    def bagi(self) :
        print("Hasil pembagian adalah ")
        if self.b == 0 :
            print("Tidak bisa melakukan operasi pembagian")
        else :  
            self.hasil = self.a / self.b
            print(f"{c} / {d} = {self.hasil}")
        print("------------------------------------")
#KELOMPOK 1
while True:
    print("Menu Kalkulator Sederhana")
    print("1. Operasi Tambah (+)")  
    print("2. Operasi Kurang (-)")
    print("3. Operasi Kali (*)")    
    print("4. Operasi Bagi (/)")
    print("0. Keluar")
    pilih = input("Pilihan Menu      : ")
    print("") 
    if pilih == '1' :    
        print("------------------------------------")
        print("\tOperasi Penjumlahan")
        c = int(input("Masukan Angka Pertama : "))
        d = int(input("Masukan Angka Kedua   : "))
        object=Tambah(c, d)
        object.tambah() 

    elif pilih == '2' :  
        print("------------------------------------")      
        print("\tOperasi Pengurangan")
        c = int(input("Masukan Angka Pertama : "))
        d = int(input("Masukan Angka Kedua   : "))
        object=Kurang(c, d)   
        object.kurang()
#KELOMPOK 1
    elif pilih == '3' :    
        print("------------------------------------")
        print("\tOperasi Perkalian")            
        c = int(input("Masukan Angka Pertama : "))
        d = int(input("Masukan Angka Kedua   : "))
        object=Kali(c, d)
        object.kali()   

    elif pilih == '4' :  
        print("------------------------------------")
        print("\tOperasi Pembagian")              
        c = int(input("Masukan Angka Pertama : "))
        d = int(input("Masukan Angka Kedua   : "))
        object=Bagi(c, d)
        object.bagi()   

    elif pilih == '0':
        print("Terima Kasih")
        break   
#KELOMPOK 1
    else :  
        print("Salah Menu, Silahkan input kembali")
    input("Enter Untuk Melanjutkan")
    
#TUGAS KELOMPOK 1
#5210411215 WILLIAM KESSLER SURdANTO
#5210411212 HAVIN NEO DIMAS NUGRAHA
#5210411232 M. TAUFIK NAMAWI
#5210411247 REVI ANANDA KIRANA PUTRI
