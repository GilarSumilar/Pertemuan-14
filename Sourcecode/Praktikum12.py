# Hitung jumlah karakter 
txt = 'Hello World'
print(len(txt),"\n")

# Ambil karakter terakhir 
print(txt[-1],"\n")

# Ambil karakter index ke-2 sampai index ke-4 (llo)
print(txt[2:5], "\n")

# Hilangkan spasi pada text tersebut (HelloWorld)
print(txt.replace(" ", "",), "\n")

# Ubah text menjadi huruf besar
print(txt.upper(), "\n")

# Ubah text menjadi huruf kecil
print(txt.lower(), "\n")

# Ganti karakter H dengan karakter J
print(txt.replace("H", "J"), "\n")

# Latihan 

umur = 24
data = 'Hai, nama saya Dito, dan umur saya adalah {} tahun'

print(data.format(umur))