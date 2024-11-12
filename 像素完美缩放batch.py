from PIL import Image
import os

def pixel_art_upscale(input_file, output_file, scale_factor=10):
    # 打开并转换为RGBA模式，以处理透明度
    with Image.open(input_file).convert("RGBA") as img:
        # 获取原始尺寸
        width, height = img.size
        
        # 计算新的尺寸
        new_width = width * scale_factor
        new_height = height * scale_factor
        
        # 创建新的图片对象，初始透明
        new_img = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))
        
        # 遍历原始图片的每个像素
        for x in range(width):
            for y in range(height):
                # 获取RGBA颜色和透明度
                color = img.getpixel((x, y))
                
                # 如果透明度为0，保持透明
                if color[3] == 0:
                    continue
                
                # 放大指定区域中的像素
                for i in range(scale_factor):
                    for j in range(scale_factor):
                        new_img.putpixel((x * scale_factor + i, y * scale_factor + j), color)
        
        # 保存新图片
        new_img.save(output_file)
        print(f"放大后的图片已保存到: {output_file}")

def batch_upscale(input_folder, output_folder, scale_factor=4):
    # 检查输入和输出文件夹是否存在
    if not os.path.exists(input_folder):
        raise ValueError(f"输入文件夹不存在: {input_folder}")
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历输入文件夹中的所有PNG图片
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):  # 只处理'png'文件
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, f"upscaled_{filename}")
            
            # 处理并放大图片
            pixel_art_upscale(input_file, output_file, scale_factor)

    print("批量处理完成！")


# 输入文件夹和输出文件夹路径
input_path = r"C:\Users\jiangran\Desktop\duolaameng"
output_path = r"C:\Users\jiangran\Desktop\duolaameng\output"

# 开始批量处理（可以修改scale_factor来改变放大倍数）
batch_upscale(input_path, output_path, scale_factor=4)
