"""改过的行：原值加 ~~删除线~~，MOD值保持 **粗体**"""
import re

md = open("mod.md", encoding="utf-8").read()
lines = md.split("\n")
out = []

for line in lines:
    m = re.match(r'^\| (.+?) \| (.+?) \| (.+?) \| (.+?) \|$', line)
    if m and m.group(1).strip() not in ("属性", "------", "奇观"):
        name = m.group(1).strip()
        orig = m.group(2).strip()
        mod_val = m.group(3).strip()
        desc = m.group(4).strip()
        if orig != mod_val and "**" in mod_val:
            # 原值加删除线，MOD值已有粗体
            line = f"| {name} | ~~{orig}~~ | {mod_val} | {desc} |"
    out.append(line)

open("mod.md", "w", encoding="utf-8").write("\n".join(out))
print("Done!")
