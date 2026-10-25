from buku import input_wajib, cari_by_kode, konfirmasi


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


