#Struktur Data
#```
Data item game
item_game = {
 "1": {"nama": "Sword", "harga": 1000},
 "2": {"nama": "Shield", "harga": 500},
 "3": {"nama": "Potion", "harga": 200}
}

Data saldo pemain
saldo = 10000
```

#Fungsi Beli Item
#```
def beli_item(item_id):
 global saldo
 if item_id in item_game:
  harga = item_game[item_id]["harga"]
  if saldo >= harga:
   saldo -= harga
   print(f"Anda berhasil membeli {item_game[item_id]['nama']}!")
  else:
   print("Saldo tidak cukup!")
 else:
  print("Item tidak tersedia!")
```

#Fungsi Tampilkan Item
#```
def tampilkan_item():
 print("Daftar Item:")
 for item_id, item in item_game.items():
  print(f"{item_id}. {item['nama']} - {item['harga']}")
```

#Fungsi Utama
#```
def main():
 global saldo
 while True:
  print("\n--- Menu ---")
  print("1. Beli Item")
  print("2. Tampilkan Item")
  print("3. Cek Saldo")
  print("4. Keluar")
  
  pilihan = input("Pilih menu: ")
  
  if pilihan == "1":
   tampilkan_item()
   item_id = input("Masukkan ID item: ")
   beli_item(item_id)
  elif pilihan == "2":
   tampilkan_item()
  elif pilihan == "3":
   print(f"Saldo: {saldo}")
  elif pilihan == "4":
   print("Terima kasih!")
   break
  else:
   print("Pilihan tidak valid!")
```

#Jalankan Program
#```
if __name__ == "__main__":
 main()
