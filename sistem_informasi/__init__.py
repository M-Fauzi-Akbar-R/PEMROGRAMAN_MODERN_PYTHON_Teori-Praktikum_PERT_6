"""Package sistem informasi mahasiswa."""

from .service.mahasiswa_service import (
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
