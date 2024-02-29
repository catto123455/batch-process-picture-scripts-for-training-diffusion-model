import os
from PIL import Image

input_folder = r"C:\Users\jiangran\Desktop\output_boom"
output_folder = r"C:\Users\jiangran\Desktop\output_boom22"

# 遍历输入文件夹中的所有png文件
# Traverse all png files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        # 创建纯白图片背景
        # Create a pure white image background
        img = Image.open(img_path)
       
        # 检查图像模式，如果不是'RGBA'，则将其转化为'RGBA'
        # Check the image mode, if it is not 'RGBA', convert it to 'RGBA'
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        white_background = Image.new('RGBA', img.size, (255, 255, 255))  #Create a white background

        # 检查图像尺寸，如果不匹配，调整尺寸
        # Check the image size and if it does not match, adjust the size
        if img.size != white_background.size:
            img = img.resize(white_background.size)

        # 将透明背景图像放置到白色背景上
        # Place a transparent background image on a white background
        white_img = Image.alpha_composite(white_background, img)

        # 保存图片，保持原名称不变
        # Save the image and keep the original name unchanged
        output_path = os.path.join(output_folder, filename)
        white_img.save(output_path)
        print("Image has been processed and saved to:", output_path)
