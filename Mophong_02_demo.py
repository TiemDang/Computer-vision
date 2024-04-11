import cv2
import numpy as np


# BAI TAP NHAN DANG HINH DANG
# Chen anh
image = cv2.imread("F:/Bai_2.jpg",) # Anh cho yeu cau 1
image_1 = cv2.imread("F:/Bai_2.jpg") # Anh cho yeu cau 1
image_2 = cv2.imread("F:/Bai_2.jpg") # Anh cho yeu cau 2
image_3 = cv2.imread("F:/Bai_2.jpg") # Anh cho yeu cau 2

# Chuyen doi anh xam thu 1
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Chuyen doi HSV cho anh xam thu 2
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Giu mau xanh
Lower_blue = np.array([90, 100, 100])
Upper_blue = np.array([157, 255, 255])
# Tao mask
Blue_mask = cv2.inRange(hsv, Lower_blue, Upper_blue)
#Ket qua sau khi giu lai mau xanh
Blue_Filter = cv2.bitwise_and(image, image, mask=Blue_mask)
# Doi result thanh anh xam thu 2
Gray_2 = cv2.cvtColor(Blue_Filter, cv2.COLOR_BGR2GRAY)
# Chuyen doi anh den trang ( ap dung cho anh xam 1 )
_, black_white = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)
# Anh 2 su dung phuong phap canny
Edges = cv2.Canny(Gray_2, 50, 150)
#Contours ( ve duong vien )
countors, hierarchy = cv2.findContours(black_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

countors_2, hierarchy_2 = cv2.findContours(Edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i, countor in enumerate(countors):
    if i == 0:
        continue
    epsilon = 0.01 * cv2.arcLength(countor, True)
    approx = cv2.approxPolyDP(countor, epsilon, True)

    cv2.drawContours(image, countor,0,(45,139,87),1)

    x, y, w, h = cv2.boundingRect(approx)

    x_mid = int(x + h/2)
    y_mid = int(y + h/2)

    coords = (x_mid, y_mid)
    color = (255,255,0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx) == 3:
        cv2.putText(image,"Tam giac",coords, font, 0.5, color, 2)
    elif len(approx) == 7:
        cv2.putText(image, " Mui ten", coords, font, 0.5, color, 2)
    else :
        cv2.putText(image, "",coords, font, 0.5, color, 2)
for z, countors in enumerate(countors_2):
    if z == 0:
        continue
    epsilon_2 = 0.03 * cv2.arcLength(countors, True)
    approx_2 = cv2.approxPolyDP(countors, epsilon_2, True)

    cv2.drawContours(image, countors,0,(45,139,87),1)

    x, y, w, h = cv2.boundingRect(approx_2)

    x_mid_2 = int(x + w/2)
    y_mid_2 = int(y + h/2)

    coords_new = (x_mid_2, y_mid_2)
    color = (255,255,0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx_2) == 3:
        cv2.putText(image,"Tam giac",coords_new, font, 0.5, color, 2)
    elif len(approx_2) == 7:
        cv2.putText(image, " Mui ten", coords_new, font, 0.5, color, 2)
    else :
        cv2.putText(image, "",coords_new, font, 0.5, color, 2)

# Nhan dang hinh dang + mau sac ( ngu giac + mau do )
HSV_0 = cv2.cvtColor(image_2, cv2.COLOR_BGR2HSV) # Doi hsv cho anh 1 de nhan dang mau
HSV_1 = cv2.cvtColor(image_3, cv2.COLOR_BGR2HSV) # Doi hsv cho anh 1 de nhan dang mau
# Giu mau do muc duoi
Lower_red_0 = np.array([0,100,100])
Upper_red_0 = np.array([20,255,255])
# Giu mau do muc tren
Lower_red_1 = np.array([171,120,120])
Upper_red_1 = np.array([200,255,255])
# Tao mask loc mau do
Red_mask_0 = cv2.inRange(HSV_0, Lower_red_0, Upper_red_0)
Red_mask_1 = cv2.inRange(HSV_1, Lower_red_1, Upper_red_1)
# Ket qua
Red_0_Filter = cv2.bitwise_and(image_2, image_2, mask= Red_mask_0)
Red_1_Filter = cv2.bitwise_and(image_3, image_3, mask= Red_mask_1)
# Gop anh
Merge = cv2.bitwise_or(Red_0_Filter,Red_1_Filter)
# Canny
Edge_0 = cv2.Canny(Merge, 50, 150)


# Ve duong vien
countors_3, hierarchy_3 = cv2.findContours(Edge_0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
for n, countorss in enumerate(countors_3):
    if n == 0:
        continue
    epsilon_3 = 0.03 * cv2.arcLength(countorss, True)
    approx_3 = cv2.approxPolyDP(countorss, epsilon_3, True)

    cv2.drawContours(image_1, countorss,0,(45,139,87),1)

    x, y, w, h = cv2.boundingRect(approx_3)

    x_mid_3 = int(x + w/2)
    y_mid_3 = int(y + h/2)

    coords_new_1 = (x_mid_3, y_mid_3)
    color = (255,255,0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx_3) == 5:
        cv2.putText(image_1,"Ngu giac do",coords_new_1, font, 0.5, color, 2)
    if len(approx_3) == 3:
        cv2.putText(image,"Tam giac",coords_new_1, font, 0.5, color, 2)
    if len(approx_3) == 7:
        cv2.putText(image,"Mui ten",coords_new_1, font, 0.5, color, 2)
    else :
        cv2.putText(image_1, "",coords_new_1, font, 0.5, color, 2)


cv2.imshow("Shape", image)
cv2.imshow("Shape + color", image_1)
# cv2.imshow("Black_white_1",black_white)
# cv2.imshow("Black_white_2 ",Edges)

# cv2.imshow("Do",Merge)
# cv2.imshow("Canny",Edge_0)
cv2.waitKey(0)
cv2.destroyAllWindows()