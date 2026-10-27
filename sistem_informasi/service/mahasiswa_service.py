"""Operasi CRUD mahasiswa dengan dictionary sebagai penyimpanan in-memory."""

from ..model import Mahasiswa

_mahasiswa = {}


def buat_mahasiswa(npm, nama, email):
    if npm in _mahasiswa:
        raise ValueError(f"Mahasiswa dengan NPM {npm} sudah terdaftar.")
    mahasiswa = Mahasiswa(npm=npm, nama=nama, email=email)
    _mahasiswa[npm] = mahasiswa.to_dict()
    return dict(_mahasiswa[npm])


def dapatkan_mahasiswa(npm):
    if npm not in _mahasiswa:
        raise KeyError(f"Mahasiswa dengan NPM {npm} tidak ditemukan.")
    return dict(_mahasiswa[npm])


def semua_mahasiswa():
    return [dict(mahasiswa) for mahasiswa in _mahasiswa.values()]


def perbarui_mahasiswa(npm, **perubahan):
    if npm not in _mahasiswa:
        raise KeyError(f"Mahasiswa dengan NPM {npm} tidak ditemukan.")
    field_diizinkan = {"nama", "email"}
    field_tidak_diizinkan = perubahan.keys() - field_diizinkan
    if field_tidak_diizinkan:
        raise ValueError(f"Field tidak dapat diubah: {', '.join(sorted(field_tidak_diizinkan))}")
    _mahasiswa[npm].update(perubahan)
    return dict(_mahasiswa[npm])


def hapus_mahasiswa(npm):
    if npm not in _mahasiswa:
        raise KeyError(f"Mahasiswa dengan NPM {npm} tidak ditemukan.")
    return _mahasiswa.pop(npm)


if __name__ == "__main__":
    buat_mahasiswa("20241320022", "Muhammad Fauzi", "fauzi@example.com")
    print(semua_mahasiswa())
