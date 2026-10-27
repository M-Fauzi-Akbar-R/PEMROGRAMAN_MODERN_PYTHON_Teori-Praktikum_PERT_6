"""Mengambil dan menganalisis post JSONPlaceholder."""

import json
from pathlib import Path

import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"


def ambil_dan_analisis(url=API_URL, min_panjang_judul=30):
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    posts = response.json()
    if not isinstance(posts, list):
        raise ValueError("Respons API harus berupa list.")

    posts_terpilih = filter(
        lambda post: isinstance(post, dict)
        and isinstance(post.get("title"), str)
        and len(post["title"]) >= min_panjang_judul,
        posts,
    )
    posts_terurut = sorted(posts_terpilih, key=lambda post: len(post["title"]), reverse=True)
    ringkasan_post = list(
        map(
            lambda post: {
                "id": post.get("id"),
                "userId": post.get("userId"),
                "title": post["title"],
                "panjang_judul": len(post["title"]),
            },
            posts_terurut,
        )
    )
    return {
        "jumlah_post_diterima": len(posts),
        "batas_minimum_panjang_judul": min_panjang_judul,
        "jumlah_post_terpilih": len(ringkasan_post),
        "post_terpilih_urut_panjang_judul": ringkasan_post,
    }


def simpan_json(data, nama_file="hasil_analisis.json"):
    path = Path(nama_file)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    return path


def main():
    hasil = ambil_dan_analisis()
    lokasi = simpan_json(hasil)
    print(f"{hasil['jumlah_post_terpilih']} post dianalisis. Hasil tersimpan di {lokasi}.")


if __name__ == "__main__":
    main()
