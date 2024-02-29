from PIL import Image
import os

input_dir = r"D:\worktimeline"
output_dir = r"D:\worktimeline"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for image_file in os.listdir(input_dir):
    if image_file.endswith('.png'):
        image_path = os.path.join(input_dir, image_file)
        img = Image.open(image_path)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save(os.path.join(output_dir, image_file), "PNG")
