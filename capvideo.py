import cv2
#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)
cap=cv2.VideoCapture(0) #获取视频设备

'''读取视频文件
cap=cv2.VideoCapture(r'C:\Users\14739\Videos\屏幕录制/a.mp4')'''

while True:
    #从摄像头读视频帧
    ret,frame=cap.read()
    #将视频帧在窗口中显示
    cv2.imshow('video',frame)
    #等待键盘事件，如果为q退出
    key=cv2.waitKey(1)
    if(key&0xFF==ord('q')):
        break
#释放VideoCapture
cap.release()
cv2.destroyAllWindows()

#视频捕捉
vc=cv2.VideoCapture('test.mp4')
#检查是否打开正确
if vc.isOpened():
    open,frame=vc.read()
else:
    open=False
    
while open:
    ret,frame=vc.read()
    if frame is None:
        break
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGRGRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(1)&0XFF==27:  '''ESC'''
        break
vc.release()
cv2.destroyAllWindows()