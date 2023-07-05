import os
import json

def convert_labelme_to_yolov5(json_path, image_width, image_height):
    with open(json_path, 'r',encoding='utf-8') as f:
        data = json.load(f)

    shapes = data['shapes']
    annotations = []

    for shape in shapes:
        label = shape['label']
        points = shape['points']

        # 转换坐标为相对值
        bbox = []
        for point in points:
            x = point[0] / image_width
            y = point[1] / image_height
            bbox.append((x, y))

        # 转换为YOLOv5格式
        x_center = (bbox[0][0] + bbox[2][0]) / 2
        y_center = (bbox[0][1] + bbox[2][1]) / 2
        width = abs(bbox[0][0] - bbox[2][0])
        height = abs(bbox[0][1] - bbox[2][1])

        class_label = ['廉颇', '小乔', '赵云', '墨子', '妲己', '嬴政', '孙尚香', '鲁班七号', '庄周', '刘禅', '高渐离', '阿轲', '钟无艳', '孙膑', '扁鹊', '白起', '芈月', '吕布', '周瑜', '夏侯惇', '甄姬', '曹操', '典韦', '宫本武藏', '李白', '马可波罗', '狄仁杰', '达摩', '项羽', '武则天', '老夫子', '关羽', '貂蝉', '安琪拉', '程咬金', '露娜', '姜子牙', '刘邦', '韩信', '王昭君', '兰陵王', '花木兰', '张良', '不知火舞', '娜可露露', '橘右京', '亚瑟', '孙悟空', '牛魔', '后羿', '刘备', '张飞', '李元芳', '虞姬', '钟馗', '成吉思汗', '杨戬', '雅典娜', '蔡文姬', '太乙真人', '哪吒', '诸葛亮', '黄忠', '大乔', '东皇太一', '干将莫邪', '鬼谷子', '铠', '百里守约', '百里玄策', '苏烈', '梦奇', '女娲', '明世隐', '公孙离', '杨玉环', '裴擒虎', '弈星', '狂铁', '米莱狄', '元歌', '孙策', '司马懿', '盾山', '伽罗', '沈梦溪', '李信', '上官婉儿', '嫦娥', '猪八戒', '盘古', '瑶', '云中君', '曜', '马超', '西施', '鲁班大师', '蒙犽', '镜', '蒙恬', '阿古朵', '夏洛特', '澜', '司空震', '艾琳', '云缨'].index(label)
        annotation = f"{class_label} {x_center} {y_center} {width} {height}"
        annotations.append(annotation)

    return annotations

# 处理指定文件夹内的所有JSON文件
json_folder = 'D:/learn/trywork/python/HOK/000'  # 替换为包含JSON文件的文件夹路径
image_folder = 'D:/learn/trywork/python/HOK/000'  # 替换为与JSON文件对应的图像文件夹路径
output_folder = 'D:/learn/trywork/python/HOK/000'  # 替换为要保存TXT文件的文件夹路径

json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]

for json_file in json_files:
    json_path = os.path.join(json_folder, json_file)
    image_file = json_file.replace('.json', '.jpg')
    image_path = os.path.join(image_folder, image_file)
    image_width, image_height = 1920,882  # 使用适当的方式获取图像的宽度和高度

    annotations = convert_labelme_to_yolov5(json_path, image_width, image_height)

    # 导出相同文件名的TXT文件
    txt_file = json_file.replace('.json', '.txt')
    txt_path = os.path.join(output_folder, txt_file)

    with open(txt_path, 'w') as f:
        for annotation in annotations:
            f.write(annotation + '\n')
