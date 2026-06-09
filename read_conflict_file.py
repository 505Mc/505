from pathlib import Path
one_folder = Path.home() / "Desktop" / "one"
file_path = one_folder / "Untitled-1.py"
content = file_path.read_bytes()
print(content.decode("utf-8", errors="replace"))