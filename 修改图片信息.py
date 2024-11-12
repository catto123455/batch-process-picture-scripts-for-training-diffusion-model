from PIL import PngImagePlugin, Image
import io

# 打开PNG图片
image_path = r'D:\图片处理工作坊\7.29\input\00032-2156776389.png'
image = Image.open(image_path)

# 获取现有的tEXt元数据
meta = image.info

# 显示现有的tEXt元数据
for k, v in meta.items():
    print(f"{k}: {v}")

# 新的参数信息
new_parameters = '''illustration of a baseball field with a baseball field and a baseball field,baseball stadium,2d game background,sunny park background,game background,2 d game art background,baseball,mobile game background,grass field,field background,stylized background,anime land of the lustrous,mobile game asset,2d game lineart behance hd,2 d game lineart behance hd,game illustration,field,open field,park background,background art,background artwork,dribbble illustration,game environment,detailed game art illustration,beautiful detailed background,art for the game,anime background key visual,2d game fanart,hockey arena game illustration,videogame background,fantasy game,game cg,lush field,
'''

# 创建一个新的PngInfo对象
meta_info = PngImagePlugin.PngInfo()

# 添加新的参数信息到PngInfo对象
meta_info.add_text("parameters", new_parameters)

# 保存图片并添加新的tEXt元数据
output_image_path = r'D:\图片处理工作坊\7.29\output\output_image.png'
image.save(output_image_path, "PNG", pnginfo=meta_info)

print(f"新参数信息已添加到 {output_image_path}")
