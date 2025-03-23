# kontrol.py
from library import hitung_umur, ramal_masa_depan

# Input data pengguna
nama = input("✨ Siapa namamu? ")
tgl_lahir = input("📅 Masukkan tanggal lahir (YYYY-MM-DD): ")

# Hitung umur
umur = hitung_umur(tgl_lahir)

if umur is None:
    print("❌ Format tanggal salah. Coba lagi!")
    exit()

# Menu utama
while True:
    print("\n🔮=== SIMULATOR RAMALAN MASA DEPAN ===🔮")
    print("1. Lihat Ramalan")
    print("2. Keluar")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        ramal_masa_depan(nama, umur)
    elif pilihan == "2":
        print(f"👋 Sampai jumpa di masa depan, {nama}!")
        break
    else:
        print("❌ Pilihan tidak valid. Coba lagi!\n")
