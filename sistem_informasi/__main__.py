"""Demo CRUD mahasiswa: jalankan dengan python -m sistem_informasi."""

from . import buat_mahasiswa, dapatkan_mahasiswa, hapus_mahasiswa, perbarui_mahasiswa


def main():
    buat_mahasiswa("20241320022", "Muhammad Fauzi Akbar Rafsanjani", "fauzi@example.com")
    print("Data awal:", dapatkan_mahasiswa("20241320022"))
    perbarui_mahasiswa("20241320022", email="fauzi.akbar@example.com")
    print("Setelah diubah:", dapatkan_mahasiswa("20241320022"))
    print("Dihapus:", hapus_mahasiswa("20241320022"))


if __name__ == "__main__":
    main()
