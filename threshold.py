import cv2
import matplotlib.pyplot as plt

# 读取图像（彩色图像，BGR格式）
img_cat = cv2.imread(r'F:\Python\opencv\OCR\img\cat.jpg')

# 阈值处理  #
# cv2.threshold(源图像, 阈值, 最大值, 阈值类型)
# 返回值：ret -> 实际使用的阈值（这里没变化）
#        thresh -> 阈值处理后的图像

# 1. BINARY 二值化
# 像素 > 127 → 255，像素 <= 127 → 0
ret, thresh1 = cv2.threshold(img_cat, 127, 255, cv2.THRESH_BINARY)

# 2. BINARY_INV 反二值化
# 像素 > 127 → 0，像素 <= 127 → 255
ret, thresh2 = cv2.threshold(img_cat, 127, 255, cv2.THRESH_BINARY_INV)

# 3. TRUNC 截断
# 像素 > 127 → 127，像素 <= 127 → 保持原值
ret, thresh3 = cv2.threshold(img_cat, 127, 255, cv2.THRESH_TRUNC)

# 4. TOZERO 保留高于阈值的像素
# 像素 > 127 → 保持原值，像素 <= 127 → 0
ret, thresh4 = cv2.threshold(img_cat, 127, 255, cv2.THRESH_TOZERO)

# 5. TOZERO_INV 反向保留高于阈值的像素
# 像素 > 127 → 0，像素 <= 127 → 保持原值
ret, thresh5 = cv2.threshold(img_cat, 127, 255, cv2.THRESH_TOZERO_INV)

# 显示结果
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img_cat, thresh1, thresh2, thresh3, thresh4, thresh5]

# 创建 2 行 3 列的子图
for i in range(6):
    plt.subplot(2, 3, i + 1)
    
    # 显示图像
    # 'gray' 参数表示用灰度显示(但是mat采用rgb，存在问题)
    plt.imshow(images[i], 'gray')
    
    # 设置子图标题
    plt.title(titles[i])
    
    # 隐藏坐标轴
    plt.xticks([]), plt.yticks([])

# 自动调整子图布局并显示
plt.show()
