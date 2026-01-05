import cv2
import numpy as np
img = cv2.imread(r'F:\Python\opencv\OCR\img\cat.jpg')

# 显示原图
cv2.imshow('img', img)
cv2.waitKey(0)           
cv2.destroyAllWindows()  

#1.均值滤波
#简单的平均卷积操作
blur = cv2.blur(img, (3,3))
cv2.imshow('blur', blur)
cv2.waitKey(0)          
cv2.destroyAllWindows()
#2.方框滤波
#基本和均值一样，可以选择归一化
box=cv2.boxFilter(img,-1,(3,3),normalize=False)
#是否归一化，如果 True → 核内像素求平均；False → 核内像素求和
cv2.imshow('box', box)
cv2.waitKey(0)          
cv2.destroyAllWindows()
#3.高斯滤波
#高斯模糊的卷积核里的数值是满足高斯分布的，相当于更重视中间的
aussian=cv2.GaussianBlur(img,(5,5),1)
cv2.imshow('aussian', aussian)
cv2.waitKey(0)          
cv2.destroyAllWindows()
#4.中值滤波
#相当于用中值替代
median=cv2.medianBlur(img,5)
cv2.imshow('median', median)
cv2.waitKey(0)          
cv2.destroyAllWindows()

#展示所有的
res=np.hstack([blur,aussian,median])
print(res)
cv2.imshow('median vs average',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

def adaptive_gaussian_smoothing(img, window_size=7, k=1.0):
    """
    自适应高斯平滑
    :param img: 输入灰度图像
    :param window_size: 局部窗口大小
    :param k: 调整平滑强度
    :return: 平滑后的图像
    """
    img = img.astype(np.float32)
    h, w = img.shape
    pad = window_size // 2
    img_padded = np.pad(img, pad, mode='reflect')
    result = np.zeros_like(img)
    
    # 逐像素计算局部标准差
    for i in range(h):
        for j in range(w):
            local_region = img_padded[i:i+window_size, j:j+window_size]
            sigma_local = np.std(local_region)  # 局部噪声估计
            sigma = k * sigma_local + 1e-5      # 避免sigma=0
            # 生成高斯核
            half_size = int(3 * sigma)
            x = np.arange(-half_size, half_size+1)
            y = np.arange(-half_size, half_size+1)
            X, Y = np.meshgrid(x, y)
            gaussian_kernel = np.exp(-(X**2 + Y**2) / (2*sigma**2))
            gaussian_kernel /= gaussian_kernel.sum()
            
            # 提取卷积区域
            region_size = 2*half_size + 1
            region = np.pad(img_padded, ((half_size, half_size),(half_size, half_size)), mode='reflect')
            local_patch = region[i:i+region_size, j:j+region_size]
            
            # 卷积得到平滑像素
            result[i, j] = np.sum(local_patch * gaussian_kernel)
    
    return result.astype(np.uint8)

# -------------------------------
# 使用示例
img = cv2.imread(r'F:\Python\opencv\OCR\img\circle.jpg', cv2.IMREAD_GRAYSCALE)
smoothed = adaptive_gaussian_smoothing(img, window_size=7, k=1.0)

cv2.imshow("Original", img)
cv2.imshow("Adaptive Gaussian Smoothed", smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()
