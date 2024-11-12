from PIL import Image
import os

def pixel_art_upscale(input_path, output_path, scale_factor=4):
    # 打开原始图片
    with Image.open(input_path).convert("RGBA") as img:
        # 获取原始尺寸
        width, height = img.size
        
        # 计算新的尺寸
        new_width = width * scale_factor
        new_height = height * scale_factor
        
        # 创建新的图片对象，保留Alpha通道
        new_img = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))
        
        # 遍历原始图片的每一个像素
        for x in range(width):
            for y in range(height):
                # 获取每个像素的RGBA值，包括透明度
                color = img.getpixel((x, y))
                
                # 如果颜色的Alpha值为0，保持透明
                if color[3] == 0:
                    continue
                
                # 在新图片中将像素扩展到指定区域
                for i in range(scale_factor):
                    for j in range(scale_factor):
                        new_img.putpixel((x*scale_factor+i, y*scale_factor+j), color)
        
        # 确保输出路径存在
        os.makedirs(output_path, exist_ok=True)
        
        # 保存新图片
        output_filename = os.path.join(output_path, f"upscaled_{os.path.basename(input_path)}")
        new_img.save(output_filename)
        print(f"放大后的图片已保存到: {output_filename}")

# 使用函数
input_path = r"C:\Users\jiangran\Desktop\meishaonvzhans\0c4628c9198246028a35d66edd7b57b2.png"
output_path = r"C:\Users\jiangran\Desktop\meishaonvzhans\output"

# 执行放大处理
pixel_art_upscale(input_path, output_path)
