from PIL import Image
import os

input_folder = r"C:\Users"
output_folder = r"C:\Users"

for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):

        img = Image.open(os.path.join(input_folder, filename))

        # 等比例放大图像10倍
        # Enlarge the image 10 times proportionally
        new_size = tuple(10 * x for x in img.size)
        img = img.resize(new_size, Image.LANCZOS)

        # 生成输出文件名并保存图像
        # Generate output file name and save image
        out_filename = os.path.join(output_folder, filename)
        img.save(out_filename)
        print(f'Image {filename} processed and saved.')
