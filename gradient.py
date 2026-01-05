import numpy as np
import cv2
img=cv2.imread(r'F:\Python\opencv\OCR\img\circle.jpg')
def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''Sobel算子'''
# 计算x方向Sobel
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
# 计算y方向Sobel
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely=cv2.convertScaleAbs(sobely)
# 计算Sobelxy
sobelxy=cv2.addWeighted(sobelx,0.5,sobelx,0.5,0)

'''Scharr算子'''
scharrx=cv2.Scharr(img,cv2.CV_64F,1,0)
scharry=cv2.Scharr(img,cv2.CV_64F,0,1)
scharrx=cv2.convertScaleAbs(scharrx)
scharry=cv2.convertScaleAbs(scharry)
scharrxy=cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

'''Laplacian算子'''
laplacian=cv2.Laplacian(img,cv2.CV_64F)
laplacian=cv2.convertScaleAbs(laplacian)
res=np.hstack([sobelxy,scharrxy,laplacian])
cv_show(res,'res')

'''Canny边缘检测
1)使用高斯滤波器，以平滑图片，滤除噪声
2)计算图像中每一个像素点的梯度强度和方向
3)应用非极大值抑制，以消除边缘检测带来的杂散响应
4)应用双阈值检测来确定真实的和潜在的边缘
5)通过抑制孤立的弱边缘最终完成边缘检测'''
img=cv2.imread(r'F:\Python\opencv\OCR\img\cat.jpg')
v1=cv2.Canny(img,80,150)
v2=cv2.Canny(img,50,100)
res=np.hstack([v1,v2])
cv_show(res,'res')
