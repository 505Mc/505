import subprocess, os
from pathlib import Path
one_folder = Path.home() / "Desktop" / "one"
os.chdir(one_folder)
print("🚀 开始推送代码到 505Mc/one 仓库...\n")
# 先切换到 main 分支（如果存在）
result = subprocess.run(["git", "checkout", "main"], capture_output=True, text=True)
print(f"切换到 main 分支: {result.stdout.strip() or result.stderr.strip()}")
# 把 1 分支的内容合并到 main
result = subprocess.run(["git", "merge", "1"], capture_output=True, text=True)
print(f"合并 1 分支到 main: {result.stdout.strip() or result.stderr.strip()}")
# 推送到远程仓库
print("\n⏫ 正在推送到 GitHub...")
result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
print(f"推送结果: {result.stdout.strip() or result.stderr.strip()}")