import subprocess, os
from pathlib import Path
one_folder = Path.home() / "Desktop" / "one"
os.chdir(one_folder)
# 提交
result = subprocess.run(["git", "commit", "-m", "合并 main 和 1 分支的内容"], capture_output=True)
print(f"git commit 返回码: {result.returncode}")
print(f"stdout: {result.stdout.decode('utf-8', errors='replace')}")
print(f"stderr: {result.stderr.decode('utf-8', errors='replace')}")
# 推送到远程
print("\n⏫ 正在推送到 GitHub...")
result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True)
print(f"git push 返回码: {result.returncode}")
print(f"stdout: {result.stdout.decode('utf-8', errors='replace')}")
print(f"stderr: {result.stderr.decode('utf-8', errors='replace')}")
if result.returncode == 0:
    print("\n✅ 上传成功！")
else:
    print("\n❌ 推送失败")