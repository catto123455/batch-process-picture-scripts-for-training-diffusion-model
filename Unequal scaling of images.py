import os
from PIL import Image

input_folder = r"C:\Users\"
output_folder = r"C:\Users\"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(os.path.join(input_folder, filename))
        resized_img = img.resize((1024, 1024))
        resized_img.save(os.path.join(output_folder, filename))
