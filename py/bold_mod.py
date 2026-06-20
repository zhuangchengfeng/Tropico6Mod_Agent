"""把 mod.md 中 MOD值 ≠ 原值 的行用 **加粗** 标记"""
import re, sys

md = open("mod.md", encoding="utf-8").read()
lines = md.split("\n")
out = []

for line in lines:
    # 匹配表格行: | 属性 | 原值 | MOD值 | 说明 |
    m = re.match(r'^\| (.+?) \| (.+?) \| (.+?) \| (.+?) \|$', line)
    if m and m.group(1).strip() not in ("属性", "------", "奇观"):
        name = m.group(1).strip()
        orig = m.group(2).strip()
        mod_val = m.group(3).strip()
        desc = m.group(4).strip()
        if orig != mod_val:
            line = f"| {name} | {orig} | **{mod_val}** | {desc} |"
    out.append(line)

open("mod.md", "w", encoding="utf-8").write("\n".join(out))
print("Done! Changed values are now bold.")
