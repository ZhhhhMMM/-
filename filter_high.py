import cv2
import numpy as np
#高通滤波->检测边缘->索贝尔算子
imge=cv2.imread(r'F:\Python\opencv\OCR\img\table_black.jpg')
# Sobel 边缘检测
d1 = cv2.Sobel(imge, cv2.CV_64F, 1, 0, ksize=5)  # X方向
d2 = cv2.Sobel(imge, cv2.CV_64F, 0, 1, ksize=5)  # Y方向
# 转换为可显示图像
abs_d1 = cv2.convertScaleAbs(d1)
abs_d2 = cv2.convertScaleAbs(d2)
# 合并边缘
dst = cv2.addWeighted(abs_d1, 0.5, abs_d2, 0.5, 0)
# 显示
cv2.imshow('Original', imge)
cv2.imshow('Sobel X', abs_d1)
cv2.imshow('Sobel Y', abs_d2)
cv2.imshow('Sobel Combined', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#高通滤波->检测边缘->沙尔算子
d3=cv2.Scharr(imge,cv2.CV_64F,1,0)
d4=cv2.Scharr(imge,cv2.CV_64F,0,1)
dst1=cv2.add(d3,d4)
cv2.imshow('dst1',dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()

##高通滤波->检测边缘->拉普拉斯算子
ldst=cv2.Laplacian(imge,cv2.CV_64F,ksize=5)
cv2.imshow('ldst',ldst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#边缘检测->Canny
dst3=cv2.Canny(imge,150,220)
cv2.imshow('dst3',dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()