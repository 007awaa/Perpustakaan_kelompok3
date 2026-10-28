from datetime import datetime

def input_wajib(pesan):
    """Minta input sampai tidak kosong. Ketik 'batal' untuk membatalkan (return None)."""
    while True:
        isi = input(pesan).strip()
        if isi.lower() == "batal":
            return None
        if isi == "":
            print("  [!] Isian tidak boleh kosong. (ketik 'batal' untuk kembali)")
            continue
        return isi
def cari_by_kode(koleksi_buku, kode):
    """Cari satu buku berdasarkan kode (tidak case sensitive). Return dict atau None."""
    for buku in koleksi_buku:
        if buku["kode_buku"].lower() == kode.lower():
            return buku
    return None

def konfirmasi(pesan):
    """Tanya y/n sampai jawabannya valid. Return True kalau 'y'."""
    while True:
        jawab = input(pesan).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  [!] Ketik 'y' untuk ya atau 'n' untuk tidak.")

def potong_teks(teks, lebar):
    """Potong teks yang terlalu panjang supaya tabel tidak berantakan."""
    if len(teks) <= lebar:
        return teks
    return teks[:lebar - 3] + "..."

def cetak_tabel(daftar_buku):
    """Cetak daftar buku dalam bentuk tabel dengan penanda status [TERSEDIA]/[DIPINJAM]."""
    garis = "-" * 108
    print(garis)
    print(f"{'No':<4}{'Kode':<10}{'Judul':<30}{'Pengarang':<20}{'Genre':<16}{'Tahun':<7}{'Status':<12}")
    print(garis)
    for nomor, b in enumerate(daftar_buku, start=1):
        penanda = "[" + b["status"].upper() + "]"
        print(f"{nomor:<4}{potong_teks(b['kode_buku'], 9):<10}"
              f"{potong_teks(b['judul'], 29):<30}"
              f"{potong_teks(b['pengarang'], 19):<20}"
              f"{potong_teks(b['genre'], 15):<16}"
              f"{b['tahun_terbit']:<7}{penanda:<12}")
    print(garis)

def tambah_buku(koleksi_buku):
    print("\n--- TAMBAH BUKU BARU ---")
    print("(ketik 'batal' kapan saja untuk kembali ke menu)")

    while True:
        kode = input_wajib("Kode buku    : ")
        if kode is None:
            print("Penambahan buku dibatalkan.")
            return
        if cari_by_kode(koleksi_buku, kode) is not None:
            print(f"  [!] Kode buku '{kode}' sudah digunakan. Gunakan kode yang berbeda.")
            continue
        break

    judul = input_wajib("Judul        : ")
    if judul is None:
            print("Penambahan buku dibatalkan.")
            return
    