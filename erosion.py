import cv2
import numpy as np
img=cv2.imread(r'F:\Python\opencv\OCR\img\blur.jpg')

'''形态学基本操作'''
# 创建一个 3x3 的卷积核（核矩阵），数据类型为 np.uint8（无符号 8 位整数）
# np.ones((3,3)) 表示全是 1 的 3x3 矩阵
kernel=np.ones((3,3),np.uint8)
# 对图像进行腐蚀操作
# erosion = cv2.erode(原图像, 卷积核, iterations=腐蚀次数)
# iterations=3 表示重复腐蚀 3 次
# 腐蚀会使图像中亮色区域（前景）变小，通常用于去噪、分离物体
erosion=cv2.erode(img,kernel,iterations=3)
# 对腐蚀后的图像进行膨胀操作
# dilate = cv2.dilate(图像, 卷积核, iterations=膨胀次数)
# 膨胀操作会使图像中亮色区域（前景）变大，通常用于恢复腐蚀后物体的大小，或者填充空洞
dige_dilate=cv2.dilate(erosion,kernel,iterations=3)
cv2.imshow('img',img)
cv2.imshow('erosion',erosion)
cv2.imshow('dilate',dige_dilate)

#开运算：先腐蚀，再膨胀
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow('opening',opening)
#闭运算：先膨胀，再腐蚀
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow('closing',closing)
#梯度运算(轮廓)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow('gradient',gradient)
#礼帽(原始输入-开运算结果)
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow('tophat',tophat)
#黑帽(闭运算-原始输入)
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('blackhat',blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
