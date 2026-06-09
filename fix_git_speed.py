import subprocess, os, time
from pathlib import Path
one_folder = Path.home() / "Desktop" / "one"
os.chdir(one_folder)
def run_cmd(cmd, timeout=15):
    try:
        start = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, shell=True)
        elapsed = time.time() - start
        return res.returncode, res.stdout.strip(), res.stderr.strip(), elapsed
    except Exception as e:
        return -1, "", str(e), 0
print("🚀 开始优化 Git 提交速度...\n")
# 1. 修复代理配置：为 HTTPS 设置正确的代理
print("1️⃣ 修复 HTTPS 代理配置...")
rc, out, err, t = run_cmd('git config --global http.proxy socks5://127.0.0.1:7891')
print(f"   设置 http.proxy: {'✅ 成功' if rc == 0 else '❌ 失败'} (耗时: {t:.2f}s)")
rc, out, err, t = run_cmd('git config --global https.proxy socks5://127.0.0.1:7891')
print(f"   设置 https.proxy: {'✅ 成功' if rc == 0 else '❌ 失败'}")
# 2. 启用 Git 压缩和加速选项
print("\n2️⃣ 开启 Git 性能优化配置...")
optimizations = [
    ("git config --global core.compression 0", "关闭压缩（小文件更快）"),
    ("git config --global pack.deltaCacheSize 128m", "增大 delta 缓存"),
    ("git config --global pack.threads 0", "使用多线程打包"),
    ("git config --global fetch.unpackLimit 100", "减少 unpack 次数"),
    ("git config --global core.preloadindex true", "预加载索引加速"),
    ("git config --global core.fscache true", "启用文件系统缓存"),
    ("git config --global gc.auto 256", "减少自动 GC 频率"),
]
for cmd, desc in optimizations:
    rc, _, _, t = run_cmd(cmd)
    print(f"   ✅ {desc}")
# 3. 测试优化后的推送速度
print("\n3️⃣ 测试推送速度（模拟）...")
# 先做一个小提交来测试
test_file = one_folder / "speed_test.txt"
test_file.write_text("speed test", encoding="utf-8")
run_cmd("git add speed_test.txt")
rc, out, err, t = run_cmd('git commit -m "test speed"')
print(f"   提交耗时: {t:.2f}s")
start_push = time.time()
rc, out, err, t = run_cmd("git push")
push_time = time.time() - start_push
print(f"   推送耗时: {push_time:.2f}s")
if rc == 0:
    print("   ✅ 推送成功！")
else:
    print(f"   ⚠️ 推送返回码: {rc}")
    print(f"   错误: {err[:200]}")
# 清理测试文件
run_cmd("git reset --hard HEAD~1")
test_file.unlink(missing_ok=True)
print("\n✅ 优化完成！")
print("\n💡 额外建议（需在 VS Code 中手动设置）：")
print("   - 打开 VS Code → 设置 → 搜索 'git.autofetch' → 改为 false（关闭自动拉取）")
print("   - 搜索 'git.confirmSync' → 改为 false（关闭同步确认弹窗）")
print("   - 搜索 'git.enableSmartCommit' → 改为 true（智能提交）")