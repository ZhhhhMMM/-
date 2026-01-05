import cv2
import numpy as np
#简单滤波实现
img=cv2.imread(r'F:\Python\opencv\OCR\img\face.jpg')
# 创建 5x5 的卷积核，所有元素为 1/25
# np.float32/25 → 相当于平均卷积核（均值滤波）
kernel=np.ones((5,5),np.float32)/25
'''# cv2.filter2D(src, ddepth, kernel)
# src: 输入图像
# ddepth: 输出图像深度，-1 表示与原图相同
# kernel: 卷积核
# dst: 输出图像'''
dst=cv2.filter2D(img,-1,kernel)
res = np.hstack([img, dst])
cv2.imshow('Original vs Filtered', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#低通滤波->去噪
#均值滤波
dst1=cv2.blur(img,(5,5))
res1=np.hstack([img,dst1])
cv2.imshow('Original vs Filtered_blur', res1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#高斯滤波
dst2=cv2.GaussianBlur(img,(5,5),sigmaX=3)
res2=np.hstack([img,dst2])
cv2.imshow('Original vs Filtered_gauss', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#中值滤波(胡椒噪音)
img2=cv2.imread(r'F:\Python\opencv\OCR\img\noise.png')
dst3=cv2.medianBlur(img2,5)
res3=np.hstack([img2,dst3])
cv2.imshow('Original vs Filtered_median', res3)
cv2.waitKey(0)
cv2.destroyAllWindows()
#双边滤波(美颜)
dst4=cv2.bilateralFilter(img,7,20,50)
res4=np.hstack([img,dst4])
cv2.imshow('Original vs Filtered_Bilater', res4)
cv2.waitKey(0)
cv2.destroyAllWindows()

