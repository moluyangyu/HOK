# HOK

兰州理工人工智能实训，图像识别王者荣耀英雄头像

训练使用默认的yolov5模型来完成，选择的是yolov5s.yaml模型文件。

训练命令为

python train.py --device 0 --img-size 1920 --batch-size 4 --epochs 1 --data C:/Users/86135/Desktop/program/new/pythonAi/data.yaml --cfg C:/Users/86135/AppData/Local/Programs/Python/Python311/yolov5/models/yolov5s.yaml --weights '' --name C:/Users/86135/Desktop/program/new/pythonAi/yolov5s_train

该命令用于开始模型训练，所有参数需要自己调整

python val.py --data C:/Users/86135/Desktop/program/new/pythonAi/data.yaml --weights C:/Users/86135/Desktop/program/new/pythonAi/yolov5s_train/weights/best.pt

该命令用于验证模型效果，所有参数需要自己调整

python detect.py --data C:/Users/86135/Desktop/program/new/pythonAi/data.yaml  --weights C:/Users/86135/Desktop/program/new/pythonAi/yolov5s_train21/weights/best.pt

该命令用于模型对图片推理，所有参数需要自己调整

调参可参考：https://zhuanlan.zhihu.com/p/516662016

train文件夹内的文件都是训练集，val文件夹内的都是验证集。

Flask文件夹内是用python快速搭建的前后端网页代码，用于展示和可视化模型推理
