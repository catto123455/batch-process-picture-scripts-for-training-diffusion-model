import os
from psd_tools import PSDImage

# 定义输入和输出路径
input_file_path = r"C:\Users\jiangran\Desktop\工作日志\2024.8.6代号王者\修改后的psd\loading.psd"
output_folder_path = r"C:\Users\jiangran\Desktop\工作日志\2024.8.6代号王者\修改后的png"

# 确保输出文件夹存在
os.makedirs(output_folder_path, exist_ok=True)

# 加载PSD文件
psd = PSDImage.open(input_file_path)

# 遍历图层并导出为PNG文件
for layer in psd:
    if layer.is_visible() and layer.has_pixels:  # 确保图层可见且为像素图层
        # 获取图层名称，替换非法字符
        layer_name = ''.join(c for c in layer.name if c.isalnum() or c in (' ', '_', '-')).rstrip()
        
        # 定义输出文件的完整路径
        output_file_path = os.path.join(output_folder_path, f"{layer_name}.png")
        
        try:
            # 导出图层为PNG文件
            layer_image = layer.topil()  # 使用topil()获取PIL图像
            
            if layer_image is not None:  # 确保 layer_image 不是 None
                layer_image.save(output_file_path, "PNG")
                print(f"导出图层 '{layer.name}' 为 PNG: {output_file_path}")
            else:
                print(f"无法导出图层 '{layer.name}': 转换为图像失败。")
        except Exception as e:
            print(f"导出图层 '{layer.name}' 时发生错误: {e}")

    else:
        print(f"跳过图层 '{layer.name}': 不是像素图层或不可见。")

print("所有可见的像素图层已处理。")
