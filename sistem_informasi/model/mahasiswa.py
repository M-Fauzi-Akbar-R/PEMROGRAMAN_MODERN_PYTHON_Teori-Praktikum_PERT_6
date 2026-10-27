"""Model data mahasiswa."""

from dataclasses import asdict, dataclass


@dataclass
class Mahasiswa:
    npm: str
    nama: str
    email: str

    def to_dict(self):
        return asdict(self)


if __name__ == "__main__":
    print(Mahasiswa("20241320022", "Muhammad Fauzi", "fauzi@example.com").to_dict())
