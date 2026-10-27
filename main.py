from buku import tambah_buku, tampilkan_semua_buku
from pencarian import cari_buku, filter_buku_by_genre
from pengelolaan import update_status_buku, hapus_buku

koleksi_buku = []

def tampilkan_menu():
    print("\n" + "=" * 40)
    print("        SISTEM PERPUSTAKAAN MINI")
    print("=" * 40)
    print("1. Tambah Buku Baru")
    print("2. Tampilkan Semua Buku")
    print("3. Cari Buku")
    print("4. Update Status Buku")
    print("5. Filter Buku Berdasarkan Genre")
    print("6. Hapus Buku")
    print("0. Keluar")
    print("-" * 40)

def menu_utama():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu [0-6]: ").strip()

        if pilihan == "1":
            tambah_buku(koleksi_buku)
        elif pilihan == "2":
            tampilkan_semua_buku(koleksi_buku)
        elif pilihan == "3":
            cari_buku(koleksi_buku)
        elif pilihan == "4":
            update_status_buku(koleksi_buku)
        elif pilihan == "5":
            filter_buku_by_genre(koleksi_buku)
        elif pilihan == "6":
            hapus_buku(koleksi_buku)
        elif pilihan == "0":
            print("\nTerima kasih. Program selesai.")
            break
        else:
            print("\n[!] Pilihan tidak valid. Masukkan angka 0 sampai 6.")


            