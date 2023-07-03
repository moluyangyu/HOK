import torch
import cv2
from models.experimental import attempt_load
from utils.general import non_max_suppression

# 加载训练好的模型
weights_path = '/path/to/best_weights.pt'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = attempt_load(weights_path, map_location=device)
model.eval()

# 进行推理
image_path = '/path/to/test/image.jpg'
img = cv2.imread(image_path)
img = torch.from_numpy(img.transpose(2, 0, 1)).float().div(255.0).unsqueeze(0).to(device)
pred = model(img)[0]
pred = non_max_suppression(pred, 0.4, 0.5)

# 处理检测结果
for det in pred:
    if det is not None and len(det):
        for *xyxy, conf, cls_id in det:
            x1, y1, x2, y2 = map(int, xyxy)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(img, 'tang_seng', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

# 显示结果图像
cv2.imshow('Inference Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
