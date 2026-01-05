import cv2
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread(r'C:\Users\14739\Pictures\shoots\a.png')
#imread 第二个参数为cv2.IMREAD_GRAYSCALE(转化灰色图)
if img is None:
    print("图片读取失败")
    exit()
    
while True:
  cv2.imshow('img', img)
  key = cv2.waitKey(0)

  if (key & 0xFF) == ord('q'):
    break

  elif (key & 0xFF) == ord('s'):
    cv2.imwrite(r'C:\Users\14739\Pictures\shoots\123.jpeg', img)
    print("图片已保存")
    
cv2.destroyAllWindows()
