import os
from PIL import Image

input_folder = r"C:\Users\jiangran\Desktop\zhipianren"
output_folder = r"C:\Users\jiangran\Desktop\正方形制片人"

# 判断输出文件夹是否存在，不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    with Image.open(os.path.join(input_folder, file_name)) as img:
        # 获取图片的长宽
        width, height = img.size
        
        # 选择长宽中最大的值作为新图片的边长
        new_length = max(width, height)
        
        # 创建新的图片，初始背景设为白色
        new_img = Image.new("RGB", (new_length, new_length), (255, 255, 255))
        
        # 如果图片有透明通道，把它和白色背景合并
        if img.mode == 'RGBA':
            img_alpha = img.split()[3]
            img = Image.composite(img, new_img, img_alpha)
            
        new_img.paste(img, ((new_length - width) // 2,
                            (new_length - height) // 2))
        
        # 保存新图片到指定文件夹
        new_img.save(os.path.join(output_folder, file_name))
        #