import cv2
import numpy as np
img=cv2.imread(r'F:\Python\opencv\OCR\img\cat.jpg')
#图像显示函数
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#截取部分图像数据
cat=img[0:200,0:200]
cv_show('cat',cat)

#颜色通道提取
'''cur_img.shape == (height, width, channel)
shape[0]	高度（行数）
shape[1]	宽度（列数）
shape[2]	通道数（BGR → 3）'''
#只保留R
cur_img=img.copy() #对原图 img 做一次深拷贝
cur_img[:,:,0]=0
cur_img[:,:,1]=0
cv_show('R',cur_img)

cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 2] = 0
cv_show('G',cur_img)

cur_img = img.copy()
cur_img[:, :, 1] = 0
cur_img[:, :, 2] = 0
cv_show('B',cur_img)