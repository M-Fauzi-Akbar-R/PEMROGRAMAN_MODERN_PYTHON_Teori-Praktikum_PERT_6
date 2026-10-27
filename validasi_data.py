"""Validasi dictionary berdasarkan schema tipe dan rentang."""


def validasi_data(data, schema, *field_wajib, **opsi):
    """Validasi data dan kembalikan (is_valid, errors).

    Schema menggunakan format:
        {"umur": {"type": int, "min": 0, "max": 120}}

    Argumen posisi tambahan adalah nama field yang wajib ada.
    Opsi keyword yang tersedia: strict_types (default True) dan
    allow_extra (default True).
    """
    if not isinstance(data, dict):
        raise TypeError("data harus berupa dictionary.")
    if not isinstance(schema, dict):
        raise TypeError("schema harus berupa dictionary.")

    opsi_tidak_dikenal = set(opsi) - {"strict_types", "allow_extra"}
    if opsi_tidak_dikenal:
        nama = ", ".join(sorted(opsi_tidak_dikenal))
        raise TypeError(f"Opsi tidak dikenal: {nama}")

    strict_types = opsi.get("strict_types", True)
    allow_extra = opsi.get("allow_extra", True)
    if not isinstance(strict_types, bool) or not isinstance(allow_extra, bool):
        raise TypeError("strict_types dan allow_extra harus berupa bool.")
    if any(not isinstance(field, str) for field in field_wajib):
        raise TypeError("Nama field wajib harus berupa string.")

    errors = []
    for field in field_wajib:
        if field not in data:
            errors.append(f"Field wajib '{field}' tidak ditemukan.")

    if not allow_extra:
        for field in data.keys() - schema.keys():
            errors.append(f"Field '{field}' tidak diizinkan.")

    for field, aturan in schema.items():
        if not isinstance(aturan, dict):
            raise TypeError(f"Aturan untuk '{field}' harus berupa dictionary.")
        expected_type = aturan.get("type")
        if expected_type is not None and not isinstance(expected_type, (type, tuple)):
            raise TypeError(f"Tipe aturan untuk '{field}' harus berupa type atau tuple type.")
        if "min" in aturan and "max" in aturan and aturan["min"] > aturan["max"]:
            raise ValueError(f"Batas minimum untuk '{field}' melebihi batas maksimum.")
        if field not in data:
            continue

        value = data[field]
        if expected_type is not None:
            if strict_types:
                valid_type = (
                    any(type(value) is item_type for item_type in expected_type)
                    if isinstance(expected_type, tuple)
                    else type(value) is expected_type
                )
            else:
                valid_type = isinstance(value, expected_type)
            if not valid_type:
                errors.append(f"Field '{field}' harus bertipe {expected_type}.")
                continue

        for batas, pembanding in (("min", lambda a, b: a >= b), ("max", lambda a, b: a <= b)):
            if batas in aturan:
                try:
                    memenuhi_batas = pembanding(value, aturan[batas])
                except TypeError:
                    memenuhi_batas = False
                if not memenuhi_batas:
                    errors.append(f"Field '{field}' harus memenuhi batas {batas}={aturan[batas]}.")

    return not errors, errors


if __name__ == "__main__":
    contoh_data = {"nama": "Fauzi", "umur": 20, "ipk": 3.6}
    contoh_schema = {
        "nama": {"type": str},
        "umur": {"type": int, "min": 17, "max": 100},
        "ipk": {"type": float, "min": 0.0, "max": 4.0},
    }
    print(validasi_data(contoh_data, contoh_schema, "nama", "umur", allow_extra=False))
