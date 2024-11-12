import os
from PIL import Image, PngImagePlugin
import re

def natural_sort_key(s):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', s)]

# 定义文件路径
txt_path = r'D:\图片处理工作坊\8.29\111.txt'
image_folder = r'D:\图片处理工作坊\8.29\改图202'

# 读取txt文件内容
with open(txt_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 确保有50行内容
if len(lines) != 51:
    print(f"警告: txt文件中的行数不是50 (实际行数: {len(lines)})")

# 获取图片文件列表并进行自然排序
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.png')], key=natural_sort_key)

# 确保有50张图片
if len(image_files) != 51:
    print(f"警告: 图片文件夹中的图片数量不是50 (实际数量: {len(image_files)})")

# 处理每张图片
for idx, (image_file, line) in enumerate(zip(image_files, lines), start=1):
    image_path = os.path.join(image_folder, image_file)
    
    # 打开图片
    with Image.open(image_path) as img:
        # 创建PngInfo对象
        meta = PngImagePlugin.PngInfo()
        
        # 添加参数信息
        meta.add_text("parameters", line.strip())
        
        # 保存图片，覆盖原文件
        img.save(image_path, "PNG", pnginfo=meta)
    
    print(f"已处理图片 {idx}/50: {image_file}")

print("所有图片处理完成。")
