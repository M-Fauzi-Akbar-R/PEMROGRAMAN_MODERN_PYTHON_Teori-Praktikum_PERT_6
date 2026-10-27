"""Menghitung statistik deskriptif sederhana untuk sekumpulan angka."""

import math
import statistics
from numbers import Real


def hitung_statistik(angka):
    """Kembalikan mean, median, modus, range, dan standard deviation populasi."""
    if not angka:
        raise ValueError("List angka tidak boleh kosong.")
    if any(not isinstance(nilai, Real) or isinstance(nilai, bool) for nilai in angka):
        raise TypeError("Semua elemen harus berupa angka.")
    if any(not math.isfinite(nilai) for nilai in angka):
        raise ValueError("Semua angka harus bernilai finite.")

    return {
        "mean": statistics.mean(angka),
        "median": statistics.median(angka),
        "modus": statistics.multimode(angka),
        "range": max(angka) - min(angka),
        "standard_deviation": statistics.pstdev(angka),
    }


if __name__ == "__main__":
    contoh = [2, 4, 4, 4, 5, 5, 7, 9]
    print(hitung_statistik(contoh))
