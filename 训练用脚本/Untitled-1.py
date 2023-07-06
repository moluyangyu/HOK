import cv2
import os

video_folder = "E:/11111111/film(2)/film"  # 替换为包含多个视频文件的文件夹路径
output_folder = "E:/11111111/111/"  # 替换为你希望保存图像文件的实际输出文件夹路径

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历视频文件夹中的每个视频文件
for video_file in os.listdir(video_folder):
    video_path = os.path.join(video_folder, video_file)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Failed to open video file:", video_file)
        continue

    # 定义每隔多少帧保存一张图像文件
    save_frequency = 50
    frame_count = 0

    # 读取视频帧
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # 保存图像文件
        if frame_count % save_frequency == 0:
            output_file = os.path.join(output_folder, os.path.splitext(video_file)[0], 'frame_{:04d}.jpg'.format(frame_count))
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            cv2.imwrite(output_file, frame)

        frame_count += 1

    cap.release()

cv2.destroyAllWindows()
