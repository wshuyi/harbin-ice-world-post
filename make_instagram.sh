#!/bin/bash
# Instagram风格图文生成器

INPUT="/home/ubuntu/.openclaw/media/inbound/file_1---3b156f89-5b02-4082-afca-b39a53e8b894.jpg"
OUTPUT="/home/ubuntu/.openclaw/media/outbound/instagram_harbin_ice_world.png"

# 获取图片信息
WIDTH=$(identify -format "%w" "$INPUT")
HEIGHT=$(identify -format "%h" "$INPUT")

# Instagram 4:5 比例目标尺寸
TARGET_W=1080
TARGET_H=1350

echo "原图尺寸: ${WIDTH}x${HEIGHT}"

# 创建渐变遮罩
convert -size 1080x300 gradient:black-transparent -alpha set -channel A -evaluate sin 50% +channel \
    -background none -gravity south \
    "$OUTPUT"

# 组合图片和文字
# 先创建基本背景
convert "$INPUT" -resize 1080x1350! -background white -gravity center \
    -extent 1080x1350 "$OUTPUT"

# 添加半透明渐变遮罩
convert "$OUTPUT" \
    -size 1080x400 gradient:black-transparent \
    -gravity south -composite \
    "$OUTPUT"

# 添加文字 - 使用ImageMagick的文本功能
# 创建文字层
convert -size 1080x300 xc:transparent -background transparent \
    -fill white -font DejaVu-Sans -pointsize 72 \
    -gravity center -annotate +0+100 "坐着火车去哈尔滨" \
    -fill "#87CEEB" -pointsize 48 \
    -annotate +0+180 "要看冰雪大世界啦！❄️" \
    -layers flatten "$OUTPUT.text.png"

# 合并文字
convert "$OUTPUT" "$OUTPUT.text.png" -gravity south -composite "$OUTPUT.final.png"

# 清理临时文件
rm -f "$OUTPUT.text.png"

echo "✅ 完成！输出: $OUTPUT.final.png"
