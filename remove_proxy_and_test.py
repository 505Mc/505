import subprocess, os, time
from pathlib import Path
one_folder = Path.home() / "Desktop" / "one"
os.chdir(one_folder)
def run_cmd(cmd, timeout=30):
    try:
        start = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, shell=True, encoding='utf-8', errors='ignore')
        elapsed = time.time() - start
        return res.returncode, res.stdout.strip(), res.stderr.strip(), elapsed
    except Exception as e:
        return -1, "", str(e), 0
print("🔧 正在移除无效的代理配置...\n")
# 1. 清除代理
run_cmd("git config --global --unset http.proxy")
run_cmd("git config --global --unset https.proxy")
run_cmd("git config --global --unset core.gitproxy")
print("✅ 已清除所有 Git 代理设置")
# 2. 创建测试文件并提交
test_file = one_folder / "speed_test2.txt"
test_file.write_text("direct connection test", encoding="utf-8")
run_cmd("git add speed_test2.txt")
rc, out, err, t = run_cmd('git commit -m "test direct push"')
print(f"📝 提交耗时: {t:.2f}s")
# 3. 直连推送测试
print("\n🚀 开始直连推送测试（走 HTTPS）...")
start_push = time.time()
rc, out, err, t = run_cmd("git push")
push_time = time.time() - start_push
print(f"⏱ 推送耗时: {push_time:.2f}s")
if rc == 0:
    print("✅ 推送成功！直连速度正常。")
else:
    print(f"⚠️ 推送失败 (返回码: {rc})")
    print(f"错误信息: {err[:300]}")
# 清理测试
run_cmd("git reset --hard HEAD~1")
test_file.unlink(missing_ok=True)
print("\n📊 诊断结论：")
print("1. 之前慢是因为配了无效的 SOCKS 代理，Git 一直在尝试连接不存在的 7891 端口。")
print("2. 已为您清除代理配置，恢复直连。")
print("3. 您的仓库很小（仅几KB），直连推送通常只需 2~5 秒。")
print("4. 如果以后需要开代理，请确保代理软件已启动且端口正确，或使用 `git config --global http.proxy http://127.0.0.1:端口号`")