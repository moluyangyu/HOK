import argparse
from flask import Flask, request, jsonify, render_template, send_file, flash
import torch
# import numpy as np
# import os
# from torchvision import transforms
# from models.experimental import attempt_load
# #from utils.plots import plot_one_box
import os
from detect import  run,main

#开始

app = Flask(__name__)

# 定义路由
@app.route('/', methods=['GET', 'POST'])  #GET和POST的请求方法
def upload():                       #upload()：回调函数
    if request.method == 'POST': 

        # 获取上传的文件

        f = request.files['file']  #函数：作用就是获取前端名为 'file'的文件信息
        global filename  # 定义全局变量
        filename = f.filename  # 获取前端上传图片名字
        global file_path  #定义全局变量
        # 将文件保存到服务器本地
        file_path = os.path.join(os.getcwd(), filename)  #本地路径+图片名字= 文件路径
        print(file_path)  # 测试程序
        f.save(file_path)  # 保存上传的图片到本地目录下，方便后续推理，找到图片
        opt = parse_opt() #调用parse_opt()函数，解析命令行参数并返回一个包含参数配置的对象opt。
        main(opt) #目标检测
    return render_template('index.html')    

# 检测结果显示
def return_img_stream(img_local_path):

    import base64   #导入base64模块，用于编码图片数据
    img_stream = ''   #创建一个空字符串变量img_stream，用于存储图片流数据。
    with open(img_local_path, 'rb') as img_f:   #打开指定路径的图片文件，使用二进制读取模式（'rb'）
        img_stream = img_f.read()     #读取图片文件的内容，并将其赋值给img_stream变量。
        img_stream = base64.b64encode(img_stream).decode()  #使用函数对图片数据进行编码，将编码后的结果转换为字符串形式。编码后的数据将存储在img_stream变量中。
    return img_stream  #返回

@app.route('/sh', methods=['GET', 'POST'])  #定义新路由，显示图片
def hello_world():
    img_path = 'runs\\detect\\exp' + str(filename) +"\\"+  str(filename) #图片路径
    img_stream = return_img_stream(img_path) #获取图片流
    return render_template('index.html', img_stream=img_stream)    #获取显示

# 检测图片（yolov5）

def parse_opt():
    parser = argparse.ArgumentParser()

    parser.add_argument('--weights', nargs='+', type=str, default= 'F:/github/HOK-1/Flask/yolov5/yolov5-master/models/yolov5s_train22/weights/best.pt', help='model path or triton URL')
    #parser.add_argument('--source', type=str, default=0, help='file/dir/URL/glob/screen/0(webcam)')
    parser.add_argument('--source', type=str, default= file_path, help='file/dir/URL/glob/screen/0(webcam)')
    parser.add_argument('--data', type=str, default= 'models/yolov5s.yaml', help='(optional) dataset.yaml path')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--project', default= 'runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp' + str(filename)  , help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--vid-stride', type=int, default=1, help='video frame-rate stride')
    opt = parser.parse_args()
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
    #print_args(vars(opt))
    args = parser.parse_args(args=[])
    print(args)
    return opt

# 启动应用
if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='0.0.0.0', port=5000)
    