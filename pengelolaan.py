from buku import input_wajib, cari_by_kode, konfirmasi
import buku


def update_status_buku(koleksi_buku):
    print("\n--- UPDATE STATUS BUKU ---")
    if len(koleksi_buku) == 0:
        print("Belum ada buku dalam koleksi.")
        return

    kode = input_wajib("Masukkan kode buku: ")
    if kode is None:
        return

    buku = cari_by_kode(koleksi_buku, kode)
    if buku is None:
        print(f"\nBuku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return

    print(f"\nJudul          : {buku['judul']}")
    print(f"Pengarang      : {buku['pengarang']}")
    print(f"Status saat ini: {buku['status']}")


    status_lama = buku["status"]
    if status_lama == "Tersedia":
        status_baru = "Dipinjam"
        kata_kerja = "dipinjam"
    else:
        status_baru = "Tersedia"
        kata_kerja = "dikembalikan"

    if konfirmasi(f"\nUbah status menjadi '{status_baru}'? (y/n): "):
        buku["status"] = status_baru
        print(f"Buku '{buku['judul']}' berhasil {kata_kerja}. "
              f"Status diubah: {status_lama} menjadi {status_baru}.")
    else:
        print("Perubahan status dibatalkan.")


def hapus_buku(koleksi_buku):
    print("\n--- HAPUS BUKU ---")
    if len(koleksi_buku) == 0:
        print("Belum ada buku dalam koleksi.")
        return

    kode = input_wajib("Masukkan kode buku yang akan dihapus: ")
    if kode is None:
        return

    buku = cari_by_kode(koleksi_buku, kode)
    if buku is None:
        print(f"\nBuku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return


    if buku["status"] == "Dipinjam":
            print(f"\nBuku '{buku['judul']}' tidak dapat dihapus karena sedang dalam status Dipinjam.")
            print("Pastikan buku dikembalikan terlebih dahulu sebelum dihapus dari koleksi.")
            return
    
    print(f"\nJudul     : {buku['judul']}")
    print(f"Pengarang : {buku['pengarang']}")
    print(f"Genre     : {buku['genre']}")
    print(f"Status    : {buku['status']}")
    
    if konfirmasi("\nYakin ingin menghapus buku ini? (y/n): "):
        koleksi_buku.remove(buku)
        print(f"Buku '{buku['judul']}' dengan kode {buku['kode_buku']} berhasil dihapus dari koleksi.")
    else:
        print("Penghapusan dibatalkan.")