"""Contoh penggunaan module utilitas_akademik."""

from utilitas_akademik import generate_transkrip, hitung_ipk, konversi_nilai_huruf


def main():
    mata_kuliah = [
        {"mata_kuliah": "Pemrograman Python", "sks": 3, "nilai": 90},
        {"mata_kuliah": "Basis Data", "sks": 3, "nilai": 82},
        {"mata_kuliah": "Matematika", "sks": 2, "nilai_huruf": "B"},
    ]
    transkrip = generate_transkrip(
        "Muhammad Fauzi Akbar Rafsanjani",
        "20241320022",
        mata_kuliah,
    )
    print("Konversi nilai 90:", konversi_nilai_huruf(90))
    print("IPK:", hitung_ipk(mata_kuliah))
    print("Transkrip:", transkrip)


if __name__ == "__main__":
    main()
