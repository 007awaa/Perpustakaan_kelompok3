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