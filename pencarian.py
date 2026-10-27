
def cari_buku(koleksi_buku):
    print("\n--- CARI BUKU ---")
    if len(koleksi_buku) == 0:
        print("Belum ada buku dalam koleksi.")
        return 

    print("Cari berdasarkan:")
    print("1. Kode buku (harus persis sama)")
    print("2. Judul buku (cukup sebagian kata)")
    mode = input("Pilih mode [1-2]: ").strip()

    if mode == "1":
            kode = input_wajib("Masukkan kode buku: ")
            if kode is None:
                return
            buku = cari_by_kode(koleksi_buku, kode)
            if buku is None:
                print(f"\nBuku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
            else:
                print("\nDitemukan 1 buku:")
                cetak_tabel([buku])

    elif mode == "2":
            kata_kunci = input_wajib("Masukkan judul/kata kunci: ")
            if kata_kunci is None:
                return

            hasil = [b for b in koleksi_buku if kata_kunci.lower() in b["judul"].lower()]
            if len(hasil) == 0:
                print(f"\nBuku dengan judul '{kata_kunci}' tidak ditemukan dalam koleksi.")
            else:
                print(f"\nDitemukan {len(hasil)} buku:")
                cetak_tabel(hasil)
    `
            

         
                