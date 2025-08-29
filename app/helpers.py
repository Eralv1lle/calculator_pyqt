def load_qss(file_name) -> str:
    with open(f"assets/qss/{file_name}", "r", encoding="utf-8") as f:
        return f.read()