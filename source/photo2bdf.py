#!/usr/bin/env python3
from PIL import Image
import numpy
import datetime
import sys
声明 = '''STARTFONT 2.1
FONT -FullPixelTest-Regular-R-Regular--12-12-75-75-c-80-iso10646-1
SIZE 12 75 75
FONTBOUNDINGBOX 12 12 0 -2
STARTPROPERTIES 10
FAMILY_NAME FullPixel (autogen)
WEIGHT_NAME Regular
FONT_VERSION 于 ''' + str(datetime.datetime.now()) + ''' 编译
COPYRIGHT (c) DWNfonts
FOUNDRY photo2bdf.py
FONT_ASCENT 10
FONT_DESCENT 2
POINT_SIZE 12
X_HEIGHT 6
CAP_HEIGHT 8
ENDPROPERTIES'''
字符数 = 0
文件 = ""


def 单区生成(欲打开的文件, 小区, 小位, U码):
    global 字符数
    if U码 < 65536:
        十六U码 = hex(U码 + 65536).split("1", 1)[1]
    else:
        十六U码 = hex(U码)
    print("STARTCHAR U+" + 十六U码)  # PS名
    图 = Image.open(欲打开的文件)
    if 图.mode != "RGBA":
        print('COMMENT 文件 ' + 欲打开的文件 + '\nCOMMENT 的格式是 ' +
              图.mode + '，而不是 RGBA。\nCOMMENT 这可能会导致字形显示成黑方形或一片空白。')
        图 = 图.convert("RGBA")
    print("ENCODING " + str(U码))  # 编码
    print('''SWIDTH 1000 0
DWIDTH 12 0
BBX 12 12 0 -2
BITMAP''')  # 杂项
    数组 = numpy.asarray(图)[小区 * 12: (小区 + 1) * 12, 小位 * 16: (小位 + 1) * 16]
    for 高 in range(12):
        二进制 = "1"
        for 宽 in range(16):
            像素 = 数组[高][宽][3]
            if 像素 > 127:
                二进制 = 二进制 + "1"
            else:
                二进制 = 二进制 + "0"
        十六进制 = hex(int(二进制, 2)).split("x1", 1)[1].upper()
        print(十六进制)
    print("ENDCHAR")
    字符数 = 字符数+1


# 测试
if sys.argv[1] == "fileHeader":
    print(声明)
elif sys.argv[1] == "genChar":
    要处理的区 = int(sys.argv[2], 16)
    for 甲 in range(16):
        for 乙 in range(16):
            单区生成(sys.argv[2] + "00.png", 甲, 乙, 要处理的区 * 256 + 甲 * 16 + 乙)