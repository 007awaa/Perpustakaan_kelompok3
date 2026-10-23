
def cari_buku(koleksi_buku):
    print("\n--- CARI BUKU ---")
    if len(koleksi_buku) == 0:
        print("Belum ada buku dalam koleksi.")
        return 

    
    print("Cari berdasarkan:")
    print("1. Kode buku (harus persis sama)")
    print("2. Judul buku (cukup sebagian kata)")
    mode = input("Pilih mode [1-2]: ").strip()