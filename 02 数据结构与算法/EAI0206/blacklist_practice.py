# 黑名单（集合）- 不许进入AI大厦的人
blacklist = {"张三", "李四", "诈骗分子A", "无证人员"}

# 今天扫码进入的人（集合）
today_visitor = {"王五", "张三", "赵六", "李四", "程序员X"}

# 交集找出不该进来的人
illegal_entries = today_visitor & blacklist

if illegal_entries:
    print("⚠️ 报警！以下人员为黑名单成员：", illegal_entries)
else:
    print("✅ 无异常，全部访客已通过身份验证")


