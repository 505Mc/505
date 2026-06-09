import subprocess, os
from pathlib import Path
one_folder = Path.home() / "Desktop" / "one"
os.chdir(one_folder)
# 合并两个版本的内容：保留 main 的 print 和 1 分支的年龄计算
merged_content = '''print("你好世界")
age = 6
add = int(input("年龄增长："))
final_age = age + add
print("你的最终年龄：", final_age)
if final_age >= 18:
    print("你成年了")
else:
    print("你未成年")
'''
file_path = one_folder / "Untitled-1.py"
file_path.write_text(merged_content, encoding="utf-8")
print("✅ 冲突已解决，文件内容已合并")
# 添加并提交
result = subprocess.run(["git", "add", "Untitled-1.py"], capture_output=True, text=True)
print(f"git add: {result.stdout.strip() or 'OK'}")
result = subprocess.run(["git", "commit", "-m", "合并 main 和 1 分支的内容"], capture_output=True, text=True)
print(f"git commit: {result.stdout.strip()}")
# 推送到远程
print("\n⏫ 正在推送到 GitHub...")
result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
print(f"推送结果: {result.stdout.strip()}")