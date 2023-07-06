import os
import shutil

def extract_files(source_folder, destination_folder):
    # 获取源文件夹中的所有文件夹
    folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

    file_counter = 1
    json_count = 0

    # 遍历每个文件夹
    for folder in folders:
        folder_path = os.path.join(source_folder, folder)

        # 获取文件夹中的所有文件
        files = os.listdir(folder_path)

        # 遍历每个文件
        for file in files:
            file_path = os.path.join(folder_path, file)

            # 检查文件类型是图片还是JSON
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # 生成新的文件名
                new_filename = f"image{file_counter}"
                file_counter += 1

                # 复制文件到目标文件夹，并重命名
                shutil.copy(file_path, os.path.join(destination_folder, f"{new_filename}.jpg"))
            elif file.lower().endswith('.json'):
                # 生成新的文件名
                new_filename = f"json{json_count}"
                json_count+=1

                # 复制文件到目标文件夹，并重命名
                shutil.copy(file_path, os.path.join(destination_folder, f"{new_filename}.json"))

extract_files('C:/Users/86135/Documents/Tencent Files/985286227/FileRecv/123456', 'C:/Users/86135/Documents/Tencent Files/985286227/FileRecv/123')
