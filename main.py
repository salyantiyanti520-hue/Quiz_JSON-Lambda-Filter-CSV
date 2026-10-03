import json
import csv

# Membaca file JSON
with open("hero.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Mengambil data hero
heroes = data["hero"]

# Filter hero dengan role EXP
hero_exp = list(filter(lambda hero: hero["role"] == "EXP", heroes))

# Transform data menggunakan lambda
hasil = list(map(lambda hero: {
    "nama": hero["nama"],
    "role": hero["role"],
    "nama_ulty": hero["nama_ulty"],
    "asal_benua": hero["asal_benua"]
}, hero_exp))

# Menampilkan hasil
print("=== HERO ROLE EXP ===")

for hero in hasil:
    print(hero)

# Menyimpan hasil ke CSV
with open("hero_exp.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["nama", "role", "nama_ulty", "asal_benua"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(hasil)

print()
print("Data berhasil disimpan ke hero_exp.csv")