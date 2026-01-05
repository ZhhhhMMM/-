import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r'F:\Python\opencv\OCR\img\cat.jpg')
top_size,bottom_size,left_size,right_size=(50,50,50,50) #定义边框大小
#在图像周围扩展边界
#1.复制边缘aaaaaa|abcdef|ffffff
replicate=cv2.copyMakeBorder(
    img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE) 
#2.镜像，不重复边缘fedcba|abcdef|fedcba
reflect=cv2.copyMakeBorder(
    img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT) 
#3.镜像，重复边缘gfedcb|abcdef|edcba
reflect101=cv2.copyMakeBorder(
    img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT_101) 
#3.循环uvwxyz|abcdef|mnopqr
wrap=cv2.copyMakeBorder(
    img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP) 
#4.常量填充,这里 0 → 黑色
constant=cv2.copyMakeBorder(
    img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value=0)

#子图布局:2行3列,当前是第 1 个(由于matplotlib采用RGB实际图片偏蓝)
plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL') 
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE') 
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT') 
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101') 
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP') 
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT') 
plt.show()

'''改进版本:
# 读取图像（OpenCV 默认读入的是 BGR 格式）
img = cv2.imread(r'F:\Python\opencv\OCR\img\cat.jpg')

# BGR → RGB
# 因为 matplotlib 显示图像时使用的是 RGB 顺序
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 设置边框的大小（上、下、左、右 各 50 像素）
top, bottom, left, right = 50, 50, 50, 50

# BORDER_REPLICATE
# 复制最边缘的像素值进行填充
replicate = cv2.copyMakeBorder(
    img, top, bottom, left, right, cv2.BORDER_REPLICATE
)

# BORDER_REFLECT
# 以边缘为轴进行镜像反射（不包含最边缘像素）
reflect = cv2.copyMakeBorder(
    img, top, bottom, left, right, cv2.BORDER_REFLECT
)

# BORDER_REFLECT_101
# 以边缘为轴镜像反射（包含最边缘像素）
reflect101 = cv2.copyMakeBorder(
    img, top, bottom, left, right, cv2.BORDER_REFLECT_101
)

# BORDER_WRAP
# 从图像的另一侧“包裹”像素进行填充（循环）
wrap = cv2.copyMakeBorder(
    img, top, bottom, left, right, cv2.BORDER_WRAP
)

# BORDER_CONSTANT
# 使用常量值填充边框，这里 value=0 表示黑色
constant = cv2.copyMakeBorder(
    img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0
)

# 将所有结果统一转换为 RGB，方便 matplotlib 显示
images = [
    img_rgb,  # 原图
    cv2.cvtColor(replicate, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(reflect, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(reflect101, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(wrap, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(constant, cv2.COLOR_BGR2RGB)
]

# 每个子图对应的标题
titles = [
    'ORIGINAL',
    'REPLICATE',
    'REFLECT',
    'REFLECT_101',
    'WRAP',
    'CONSTANT'
]

# 创建画布，大小为 10×6 英寸
plt.figure(figsize=(10, 6))

# 循环绘制 6 张图
for i in range(6):
    # 2 行 3 列的子图，第 i+1 个位置
    plt.subplot(2, 3, i + 1)
    
    # 显示图像
    plt.imshow(images[i])
    
    # 设置子图标题
    plt.title(titles[i])
    
    # 关闭坐标轴显示
    plt.axis('off')

# 自动调整子图间距，防止重叠
plt.tight_layout()

# 显示所有图像
plt.show()


'''