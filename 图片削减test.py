import os
from PIL import Image

# 输入目录和输出目录
input_folder = r"D:\图片处理工作坊\9.12\去除边缘"
output_folder = r"D:\图片处理工作坊\9.12\输出"

# 确保输出目录存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 宽度和高度减少的像素数
WIDTH_REDUCE = 20
HEIGHT_REDUCE = 20

for file_name in os.listdir(input_folder):
    if file_name.endswith('.png'):
        with Image.open(os.path.join(input_folder, file_name)) as img:
            width, height = img.size

            # 计算新的宽度和高度
            new_width = max(1, width - 2 * WIDTH_REDUCE)
            new_height = max(1, height - 2 * HEIGHT_REDUCE)

            # 裁剪图片
            left = WIDTH_REDUCE
            upper = HEIGHT_REDUCE
            right = width - WIDTH_REDUCE
            lower = height - HEIGHT_REDUCE

            cropped_img = img.crop((left, upper, right, lower))

            # 创建一个新的背景透明的图像
            new_img = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

            # 将裁剪后的图像粘贴到新的图像背景上
            new_img.paste(cropped_img, (0, 0))

            # 保存处理后的图片
            new_img.save(os.path.join(output_folder, file_name))

print("处理完成")
