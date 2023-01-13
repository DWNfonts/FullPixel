import os
import re
k = 0
for a in os.listdir("."):
    if a.endswith(".png"):
        k = k + 1
os.system("python3 ./photo2bdf.py fileHeader")
print("CHARS " + str(k * 256))
for i in os.listdir("."):
    if i.endswith(".png"):
        j = i.replace("00.png", "")
        os.system("python3 ./photo2bdf.py genChar " + j)
    else:
        print("COMMENT " + i + " 不是 png 图片。")
print('''COMMENT 注意，某些情况下 CHARS 可能会偏后，
COMMENT 但是如果您的字体编辑器 / 查看器不支持这种“特例”，
COMMENT 请把 CHARS 靠前。
ENDFONT''')
