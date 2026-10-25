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