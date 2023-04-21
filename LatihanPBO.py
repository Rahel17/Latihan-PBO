#Soal No.1 
#Program untuk mengecek apakah suatu objek merupakan palindrome (Functional Programming)
def is_palindrome(object):
    n = len(object)
    i = 0
    palindrome = True

    while i <= n//2 and palindrome == True:
        if object[i] != object[n-i-1]:
            palindrome = False
        i += 1
    
    return palindrome

input_object = input("Masukkan Objek : ")

if is_palindrome(input_object):
    print("Objek merupakan palindrome")
else :
    print("Objek bukan palindrome")


#Program Object Oriented Sederhana
class Buah:
    def __init__(self, nama, rasa, warna):
        self.nama = nama
        self.rasa = rasa
        self.warna = warna

    def deskripsi(self):
        print(f"Buah {self.nama} berwarna {self.warna} dan rasanya {self.rasa}.")

    def dimakan(self):
        print(f"Anda sedang makan {self.nama}... Enak sekali!")

# Membuat objek buah1 dan buah2
buah1 = Buah("Mangga", "manis", "kuning")
buah2 = Buah("Apel", "asam", "merah")

# Memanggil metode deskripsi() pada buah1 dan buah2
buah1.deskripsi()
buah2.deskripsi()

# Memanggil metode dimakan() pada buah1 dan buah2
buah1.dimakan()
buah2.dimakan()

