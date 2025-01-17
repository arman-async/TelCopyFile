from pathlib import Path


class Binary:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def add_to_end(self, beyte_len: int):
        with open(self.file_path, "ab") as f:
            f.write(b"\x00" * beyte_len)
