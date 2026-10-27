"""Layanan package sistem_informasi."""

from .mahasiswa_service import (
    buat_mahasiswa,
    dapatkan_mahasiswa,
    hapus_mahasiswa,
    perbarui_mahasiswa,
    semua_mahasiswa,
)

__all__ = [
    "buat_mahasiswa",
    "dapatkan_mahasiswa",
    "hapus_mahasiswa",
    "perbarui_mahasiswa",
    "semua_mahasiswa",
]
