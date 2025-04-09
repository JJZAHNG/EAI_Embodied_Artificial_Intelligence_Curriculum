whitelist = {"王五", "赵六", "程序员X"}
blacklist = {"李四", "诈骗分子"}
today_visitor = {}

for person in today_visitor:
    if person in blacklist:
        print(f"{person} ❌ 拒绝进入")
    elif person in whitelist:
        print(f"{person} ✅ 欢迎光临")
    else:
        print(f"{person} ⚠️ 身份未知，请人工核实")
