"""Fungsi bantu untuk menampilkan data mahasiswa."""


def format_mahasiswa(mahasiswa):
    return f"{mahasiswa['npm']} - {mahasiswa['nama']} ({mahasiswa['email']})"


if __name__ == "__main__":
    print(format_mahasiswa({
        "npm": "20241320022",
        "nama": "Muhammad Fauzi",
        "email": "fauzi@example.com",
    }))
