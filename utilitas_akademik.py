"""Fungsi akademik sederhana untuk nilai dan transkrip mahasiswa."""


_BOBOT_NILAI = {
    "A": 4.0,
    "AB": 3.5,
    "B": 3.0,
    "BC": 2.5,
    "C": 2.0,
    "D": 1.0,
    "E": 0.0,
}


def konversi_nilai_huruf(nilai):
    """Konversi nilai angka 0-100 menjadi nilai huruf."""
    if not isinstance(nilai, (int, float)) or isinstance(nilai, bool):
        raise TypeError("Nilai harus berupa angka.")
    if not 0 <= nilai <= 100:
        raise ValueError("Nilai harus berada pada rentang 0 sampai 100.")
    if nilai >= 85:
        return "A"
    if nilai >= 80:
        return "AB"
    if nilai >= 75:
        return "B"
    if nilai >= 70:
        return "BC"
    if nilai >= 65:
        return "C"
    if nilai >= 50:
        return "D"
    return "E"


def _nilai_huruf(mata_kuliah):
    if "nilai_huruf" in mata_kuliah:
        nilai = mata_kuliah["nilai_huruf"].upper()
        if nilai not in _BOBOT_NILAI:
            raise ValueError(f"Nilai huruf tidak dikenal: {nilai}")
        return nilai
    if "nilai" in mata_kuliah:
        return konversi_nilai_huruf(mata_kuliah["nilai"])
    raise ValueError("Setiap mata kuliah harus memiliki 'nilai' atau 'nilai_huruf'.")


def hitung_ipk(mata_kuliah):
    """Hitung IPK berbobot SKS dari daftar dictionary mata kuliah."""
    daftar = list(mata_kuliah)
    if not daftar:
        raise ValueError("Daftar mata kuliah tidak boleh kosong.")

    total_sks = 0
    total_bobot = 0.0
    for matkul in daftar:
        if not isinstance(matkul, dict):
            raise TypeError("Setiap mata kuliah harus berupa dictionary.")
        sks = matkul.get("sks")
        if not isinstance(sks, (int, float)) or isinstance(sks, bool) or sks <= 0:
            raise ValueError("SKS setiap mata kuliah harus berupa angka positif.")
        huruf = _nilai_huruf(matkul)
        total_sks += sks
        total_bobot += _BOBOT_NILAI[huruf] * sks
    return round(total_bobot / total_sks, 2)


def generate_transkrip(nama, npm, mata_kuliah):
    """Buat dictionary transkrip beserta IPK mahasiswa."""
    mata_kuliah = list(mata_kuliah)
    daftar = []
    for matkul in mata_kuliah:
        huruf = _nilai_huruf(matkul)
        daftar.append(
            {
                "mata_kuliah": matkul["mata_kuliah"],
                "sks": matkul["sks"],
                "nilai_huruf": huruf,
            }
        )
    return {
        "nama": nama,
        "npm": npm,
        "mata_kuliah": daftar,
        "ipk": hitung_ipk(mata_kuliah),
    }


if __name__ == "__main__":
    contoh = [
        {"mata_kuliah": "Pemrograman Python", "sks": 3, "nilai": 90},
        {"mata_kuliah": "Basis Data", "sks": 3, "nilai_huruf": "AB"},
    ]
    print(generate_transkrip("Muhammad Fauzi", "20241320022", contoh))
