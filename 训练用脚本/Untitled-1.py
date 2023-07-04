import cv2

video_path = 'C:/Users/86135/Desktop/program/new/pythonAi/西游记10.mp4'
output_folder = 'C:/Users/86135/Desktop/program/new/pythonAi/picture/'

# 打开视频文件
video_capture = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not video_capture.isOpened():
    print("无法打开视频文件")
    exit()

# 逐帧读取视频并保存为图像文件
frame_count = 0
while True:
    success, frame = video_capture.read()

    # 检查是否成功读取帧
    if not success:
        break

    # 保存图像文件
    output_file = output_folder + 'frame_{:04d}.jpg'.format(frame_count)
    cv2.imwrite(output_file, frame)

    frame_count += 1

# 释放视频资源
video_capture.release()
#python train.py --img 768*576 --batch 16 --epochs 50 --data C:/Users/86135/Desktop/program/new/pythonAi/data.yaml --cfg C:/Users/86135/AppData/Local/Programs/Python/Python310/yolov5/models/yolov5m.yaml  --name C:/Users/86135/Desktop/program/new/pythonAi/yolov5s_tang_seng
#python train.py --device 0 --img-size 768 --batch-size 21 --epochs 100 --data C:/Users/86135/Desktop/program/new/pythonAi/data.yaml --cfg C:/Users/86135/AppData/Local/Programs/Python/Python310/yolov5/models/yolov5s.yaml --weights '' --name C:/Users/86135/Desktop/program/new/pythonAi/yolov5s_train
#python val.py --data C:/Users/86135/Desktop/program/new/pythonAi/data.yaml --weights C:/Users/86135/Desktop/program/new/pythonAi/yolov5s_train2/weights/best.pt
