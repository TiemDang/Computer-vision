import cv2
import numpy as np


# BAI TAP NHAN DANG HINH DANG
# Chen anh
image = cv2.imread("F:/Bai_2.jpg",)
image_1 = cv2.imread("F:/Bai_2.jpg")
image_2 = cv2.imread("F:/Bai_2.jpg")
image_3 = cv2.imread("F:/Bai_2.jpg")


# Chuyen doi HSV
#1
Blue_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#2
Pink_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#3
Yellow_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#4
Red_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#5
Green_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#6
White_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Giu mau
# 1.Blue
Lower_blue = np.array([90, 100, 100])
Upper_blue = np.array([157, 255, 255])
# 2.Pink
Lower_pink = np.array([140,50,20])
Upper_pink = np.array([174,255,255])
# # 3 Yellow
# Lower_yellow = np.array()
# Upper_yellow = np.array()
# # 4.1 Red (1)
# Lower_red_0 = np.array()
# Upper_red_0 = np.array()
# # 4.2 Red(2)
# Lower_red_1 = np.array()
# Upper_red_1 = np.array()
# # 5.Green
# Lower_green = np.array()
# Upper_green = np.array()
# # 6.White
# Lower_white = np.array()
# Upper_white = np.array()




# Tao mask
# 1.Blue
Blue_mask = cv2.inRange(Blue_hsv, Lower_blue, Upper_blue)
# # 2. Pink
Pink_mask = cv2.inRange(Pink_hsv, Lower_pink, Upper_pink)
# # 3. Yellow
# Yellow_mask = cv2.inRange(Yellow_hsv, Lower_yellow, Upper_yellow)
# # 4. Red
# # 4.1 Red_0
# Red_mask_0 = cv2.inRange(Red_hsv, Lower_red_0, Upper_red_0)
# # 4.2 Red_1
# Red_mask_1 = cv2.inRange(Red_hsv, Lower_red_1, Upper_red_1)
# # 5. Green
# Green_mask = cv2.inRange(Green_hsv, Lower_green, Upper_green)
# # 6. White
# White_mask = cv2.inRange(White_hsv, Lower_white, Upper_white)

#Ket qua sau khi giu mau
Blue_Filter = cv2.bitwise_and(image, image, mask=Blue_mask)
Pink_Filter = cv2.bitwise_and(image, image, mask=Pink_mask)
# Yellow_Filter = cv2.bitwise_and(image, image, mask=Yellow_mask)
# #
# Red_0_Filter = cv2.bitwise_and(image, image, mask= Red_mask_0)
# Red_1_Filter = cv2.bitwise_and(image_3, image_3, mask= Red_mask_1)
# Merge = cv2.bitwise_or(Red_0_Filter,Red_1_Filter)
# #
# Green_Filter = cv2.bitwise_and(image, image, mask=Green_mask)
# #
# White_filter = cv2.bitwise_and(image, image, mask=White_mask)

# Anh 2 su dung phuong phap canny
Edges_Blue = cv2.Canny(Blue_Filter, 50, 150)
Edges_Pink = cv2.Canny(Pink_Filter, 50, 150 )
#Contours ( ve duong vien )
# countors_, hierarchy = cv2.findContours(black_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

Countors_Blue, Hierarchy_Blue = cv2.findContours(Edges_Blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

Countors_Pink, Hierarchy_Pink = cv2.findContours(Edges_Pink, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for i, countor in enumerate(countors):
#     if i == 0:
#         continue
#     epsilon = 0.01 * cv2.arcLength(countor, True)
#     approx = cv2.approxPolyDP(countor, epsilon, True)
#
#     cv2.drawContours(image, countor,0,(45,139,87),1)
#
#     x, y, w, h = cv2.boundingRect(approx)
#
#     x_mid = int(x + h/2)
#     y_mid = int(y + h/2)
#
#     coords = (x_mid, y_mid)
#     color = (255,255,0)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#
#     if len(approx) == 3:
#         cv2.putText(image,"Tam giac",coords, font, 0.5, color, 2)
#     elif len(approx) == 7:
#         cv2.putText(image, " Mui ten", coords, font, 0.5, color, 2)
#     else :
#         cv2.putText(image, "",coords, font, 0.5, color, 2)
for z, countors in enumerate(Countors_Blue):
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

for p, countors in enumerate(Countors_Pink):
    if p == 0:
        continue
    epsilon_pink = 0.03 * cv2.arcLength(countors, True)
    approx_pink = cv2.approxPolyDP(countors, epsilon_pink, True)

    cv2.drawContours(image, countors,0,(45,139,87),1)

    x, y, w, h = cv2.boundingRect(approx_pink)

    x_mid_2 = int(x + w/2)
    y_mid_2 = int(y + h/2)

    coords_new = (x_mid_2, y_mid_2)
    color = (255,255,0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx_pink) == 3:
        cv2.putText(image,"Tam giac",coords_new, font, 0.5, color, 2)
    elif len(approx_pink) == 7:
        cv2.putText(image, " Mui ten", coords_new, font, 0.5, color, 2)
    else :
        cv2.putText(image, "",coords_new, font, 0.5, color, 2)

# Nhan dang hinh dang + mau sac ( ngu giac + mau do )
# HSV_0 = cv2.cvtColor(image_2, cv2.COLOR_BGR2HSV) # Doi hsv cho anh 1 de nhan dang mau
# HSV_1 = cv2.cvtColor(image_3, cv2.COLOR_BGR2HSV) # Doi hsv cho anh 1 de nhan dang mau
# # Giu mau do muc duoi
# Lower_red_0 = np.array([0,100,100])
# Upper_red_0 = np.array([20,255,255])
# # Giu mau do muc tren
# Lower_red_1 = np.array([171,120,120])
# Upper_red_1 = np.array([200,255,255])
# # Tao mask loc mau do
# Red_mask_0 = cv2.inRange(HSV_0, Lower_red_0, Upper_red_0)
# Red_mask_1 = cv2.inRange(HSV_1, Lower_red_1, Upper_red_1)
# # Ket qua
# Red_0_Filter = cv2.bitwise_and(image_2, image_2, mask= Red_mask_0)
# Red_1_Filter = cv2.bitwise_and(image_3, image_3, mask= Red_mask_1)
# # Gop anh
# Merge = cv2.bitwise_or(Red_0_Filter,Red_1_Filter)
# # Canny
# Edge_0 = cv2.Canny(Merge, 50, 150)


# Ve duong vien
# countors_3, hierarchy_3 = cv2.findContours(Edge_0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
# for n, countorss in enumerate(countors_3):
#     if n == 0:
#         continue
#     epsilon_3 = 0.03 * cv2.arcLength(countorss, True)
#     approx_3 = cv2.approxPolyDP(countorss, epsilon_3, True)
#
#     cv2.drawContours(image_1, countorss,0,(45,139,87),1)
#
#     x, y, w, h = cv2.boundingRect(approx_3)
#
#     x_mid_3 = int(x + w/2)
#     y_mid_3 = int(y + h/2)
#
#     coords_new_1 = (x_mid_3, y_mid_3)
#     color = (255,255,0)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#
#     if len(approx_3) == 5:
#         cv2.putText(image_1,"Ngu giac do",coords_new_1, font, 0.5, color, 2)
#     if len(approx_3) == 3:
#         cv2.putText(image,"Tam giac",coords_new_1, font, 0.5, color, 2)
#     if len(approx_3) == 7:
#         cv2.putText(image,"Mui ten",coords_new_1, font, 0.5, color, 2)
#     else :
#         cv2.putText(image_1, "",coords_new_1, font, 0.5, color, 2)

cv2.imshow("Result",image)
# cv2.imshow("Gray_B",Pink_Filter)
# cv2.imshow("Edges_B", Edges_Pink)
cv2.waitKey(0)
cv2.destroyAllWindows()