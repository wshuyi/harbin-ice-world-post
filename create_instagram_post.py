#!/usr/bin/env python3
"""
Instagram风格个人页面生成器
为帅气的男孩制作火车去哈尔滨看冰雪大世界的分享图
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_instagram_post():
    # 读取原图
    original_path = "/home/ubuntu/.openclaw/media/inbound/file_1---3b156f89-5b02-4082-afca-b39a53e8b894.jpg"
    img = Image.open(original_path)
    
    # Instagram 4:5 比例 (1080x1350)
    target_width = 1080
    target_height = 1350
    
    # 创建设计底板
    background = Image.new('RGB', (target_width, target_height), '#FFFFFF')
    
    # 计算缩放比例 - 保持宽度适应
    scale = target_width / img.width
    new_height = int(img.height * scale)
    
    # 居中放置图片
    resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
    img_y = (target_height - new_height) // 2
    
    # 粘贴图片到背景
    background.paste(resized_img, (0, img_y))
    
    # 添加半透明黑色渐变遮罩用于文字显示
    overlay = Image.new('RGBA', (target_width, target_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # 在底部添加文字区域 - 半透明黑色渐变
    text_height = 300
    gradient_height = text_height
    
    # 从下往上创建渐变
    for y in range(target_height - gradient_height, target_height):
        # 计算透明度：底部完全不透明，向上渐变
        y_pos = y - (target_height - gradient_height)
        alpha = int(255 * (y_pos / gradient_height) ** 0.5)
        
        # 创建渐变条
        draw.line([(0, y), (target_width, y)], fill=(0, 0, 0, alpha), width=1)
    
    # 将遮罩层合到背景上
    background = Image.alpha_composite(background.convert('RGBA'), overlay).convert('RGB')
    
    # 重新创建draw对象
    draw = ImageDraw.Draw(background)
    
    # 加载字体
    try:
        font_paths = [
            "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
            "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc", 
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ]
        
        font = None
        for font_path in font_paths:
            if os.path.exists(font_path):
                font = ImageFont.truetype(font_path, size=72)
                break
        
        if font is None:
            font = ImageFont.load_default()
            
    except Exception as e:
        print(f"字体加载失败，使用默认字体: {e}")
        font = ImageFont.load_default()
    
    # 添加文字
    main_text = "坐着火车去哈尔滨"
    sub_text = "要看冰雪大世界啦！✨"
    
    # 文字位置 - 在底部居中
    text_y_start = target_height - 260
    
    # 主标题
    try:
        bbox = draw.textbbox((0, 0), main_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (target_width - text_width) // 2
    except:
        text_x = target_width // 2 - len(main_text) * 20
    
    # 绘制主标题
    draw.text((text_x, text_y_start), main_text, fill='#FFFFFF', font=font, align='center')
    
    # 副标题
    try:
        font_sub_size = int(font.size * 0.67) if hasattr(font, 'size') else 48
        if hasattr(font, 'fname'):
            font_sub = ImageFont.truetype(font.fname, size=font_sub_size)
        else:
            font_sub = font
        bbox = draw.textbbox((0, 0), sub_text, font=font_sub)
        sub_width = bbox[2] - bbox[0]
        sub_x = (target_width - sub_width) // 2
    except:
        sub_x = target_width // 2 - len(sub_text) * 12
        font_sub = font
    
    draw.text((sub_x, text_y_start + 90), sub_text, fill='#87CEEB', font=font_sub, align='center')
    
    # 添加雪花装饰
    draw_emoji(draw, target_width, target_height, font)
    
    # 保存图片
    output_path = "/home/ubuntu/.openclaw/media/outbound/instagram_harbin_ice_world.png"
    background.save(output_path, 'PNG', quality=95)
    
    print(f"✅ Instagram风格图片已生成：{output_path}")
    print(f"📐 尺寸: {target_width}x{target_height}")
    return output_path

def draw_emoji(draw, width, height, font):
    """在图片上添加雪花装饰"""
    import random
    snowflakes = ['❄️', '❅', '❆', '✦', '✧']
    
    # 在顶部区域随机放置雪花
    for _ in range(15):
        x = random.randint(50, width - 50)
        y = random.randint(50, 300)
        emoji = random.choice(snowflakes)
        
        try:
            draw.text((x, y), emoji, font=font)
        except:
            pass

if __name__ == "__main__":
    create_instagram_post()
