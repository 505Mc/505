import subprocess, os
from pathlib import Path
one_folder = Path.home() / "Desktop" / "one"
os.chdir(one_folder)
# 查看冲突文件内容
print("=== 冲突文件内容 ===")
result = subprocess.run(["git", "diff"], capture_output=True, text=True)
print(result.stdout)
# 查看当前状态
print("\n=== 当前状态 ===")
result = subprocess.run(["git", "status"], capture_output=True, text=True)
print(result.stdout)