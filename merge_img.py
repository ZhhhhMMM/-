import cv2
import numpy as np
import matplotlib.pyplot as plt
img_cat=cv2.imread(r'F:\Python\opencv\OCR\img\cat.jpg')
img_dog=cv2.imread(r'F:\Python\opencv\OCR\img\dog.jpg') 
print(img_cat.shape)
print(img_dog.shape)
img_dog=cv2.resize(img_dog,(800,800))
print(img_dog.shape)
# 按比例放大图像
#cv2.resize(src, dsize, fx=0, fy=0, interpolation=cv2.INTER_LINEAR)
# cv2.resize() 用于调整图像大小
# dsize=(0,0) 表示不指定目标绝对尺寸，而使用 fx 和 fy 进行缩放
# fx=4 表示水平方向放大 4 倍
# fy=4 表示垂直方向放大 4 倍
# 默认使用双线性插值（INTER_LINEAR），放大后图像平滑
#img_dog=cv2.resize(img_dog,(0,0),fx=4,fy=4)

# 图像加权融合
# 将 img_cat 和 img_dog 按比例混合生成新图像 res
# img_cat 的权重 alpha = 0.4
# img_dog 的权重 beta = 0.6
# gamma = 0 表示不加额外亮度
# 公式：res = img_cat*0.4 + img_dog*0.6 + 0
res = cv2.addWeighted(img_cat, 0.4, img_dog, 0.6, 0)
plt.imshow(res)
plt.show()