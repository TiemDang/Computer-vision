import cv2
import numpy as np

# Đọc ảnh gốc
img_0 = cv2.imread('F:/Bai_2.jpg')  # 0 để đọc ảnh ở chế độ grayscale
img_1 = cv2.imread('F:/Bai_2.jpg')

# Chuyen doi hsv
hsv_0 = cv2.cvtColor(img_0, cv2.COLOR_BGR2HSV)
hsv_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)
# Giu mau do vung 1
Lower_red_0 = np.array([0,100,100])
Upper_red_0 = np.array([25,255,255])
# Giu mau do vung 2
Lower_red_1 = np.array([171,120,120])
Upper_red_1 = np.array([200,255,255])
# Tao mask
red_mask_0 = cv2.inRange(hsv_0, Lower_red_0, Upper_red_0)
red_mask_1 = cv2.inRange(hsv_1, Lower_red_1, Upper_red_1)
# Loc
Red_0_Filter = cv2.bitwise_and(img_0,img_0, mask=red_mask_0)
Red_1_Filter = cv2.bitwise_and(img_1,img_1, mask=red_mask_1)
# gop anh
Merge = cv2.bitwise_or(Red_0_Filter,Red_1_Filter)



cv2.imshow("Do muc thap",Red_0_Filter)
cv2.imshow("Do muc cao", Red_1_Filter)
cv2.imshow("Gop anh", Merge)
cv2.waitKey(0)
cv2.destroyAllWindows()
