objects = {
    "obj1": {"颜色": "红", "位置": (1, 2)},
    "obj2": {"颜色": "蓝", "位置": (3, 4)},
    "obj3": {"颜色": "红", "位置": (2, 2)},
}

for name, info in objects.items():
    if info["颜色"] == "红":
        print("匹配到：", name)


