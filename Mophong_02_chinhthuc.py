import cv2
import numpy as np


# BAI TAP NHAN DANG HINH DANG
# Chen anh
image = cv2.imread("F:/Bai_2.jpg",) # Anh cho yeu cau 1
image_1 = cv2.imread("F:/Bai_2.jpg") # Anh cho yeu cau 1
img_0 = cv2.imread("F:/Bai_2.jpg") # Anh cho yeu cau 2
img_1 = cv2.imread("F:/Bai_2.jpg") # Anh cho yeu cau 2



# Chuyen doi HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_pink = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Giu mau
#---------------------------------------
# Giu mau xanh duong
lower_blue = np.array([90,100,100])
upper_blue = np.array([157,255,255])
# Giu mau vang
lower_yellow = np.array([12,100,100])
upper_yellow = np.array([50,255,255])
# Giu mau xanh la
lower_green = np.array([35,100,100])
upper_green = np.array([110,255,255])
# Giu mau hong
lower_pink = np.array([210,100,100])
upper_pink = np.array([255,200,255])
# Giu mau trang
lower_white = np.array([199,199,199])
upper_white = np.array([255,255,255])

# Tao mask
#--------------------------------------------------
# Mask blue
mask_blue = cv2.inRange(hsv, lower_blue,upper_blue)
# Mask yellow
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
# Mask green
mask_green = cv2.inRange(hsv, lower_green, upper_green)
# Mask pink
mask_pink = cv2.inRange(hsv_pink, lower_pink, upper_pink)
# Mask white
mask_white = cv2.inRange(hsv_pink, lower_white, upper_white)

# Ket qua sau khi dung bo loc
#--------------------------------------------------
# Ket qua sau khi giu lai mau xanh duong
Blue = cv2.bitwise_and(image,image, mask=mask_blue)
# Ket qua sau khi giu mau vang
Yellow =cv2.bitwise_and(image, image, mask=mask_yellow)
# Ket qua sau khi giu mau xanh la
Green = cv2.bitwise_and(image, image, mask=mask_green)
# Ket qua sau khi giu mau hong
Pink = cv2.bitwise_and(image, image, mask=mask_pink)
# Ket qua sau khi giu anh trang
White = cv2.bitwise_and(image, image, mask=mask_white)

# Doi ket qua thanh anh xam
Blue_gray = cv2.cvtColor(Blue, cv2.COLOR_BGR2GRAY)
Yellow_gray = cv2.cvtColor(Yellow, cv2.COLOR_BGR2GRAY)
Green_gray = cv2.cvtColor(Green, cv2.COLOR_BGR2GRAY)
Pink_gray = cv2.cvtColor(Pink, cv2.COLOR_BGR2GRAY)
White_gray = cv2.cvtColor(White, cv2.COLOR_BGR2GRAY)


# Phuong phap canny
#----------------------------------------------------------
Blue_edges = cv2.Canny(Blue_gray, 50, 150)
Yellow_edge = cv2.Canny(Yellow_gray, 50, 150)
Green_edge = cv2.Canny(Green_gray, 30, 150 )
Pink_edge = cv2.Canny(Pink_gray, 20 ,150)
White_edge = cv2.Canny(White_gray,20,200)


#Contours ( ve duong vien )
#---------------------------------------------------------
Yellow_countors, hierarchy = cv2.findContours(Yellow_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

Blue_countors, hierarchy_2 = cv2.findContours(Blue_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

Green_countors, hierarchy_green = cv2.findContours(Green_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

Pink_countors, hierarchy_pink = cv2.findContours(Pink_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

White_countors, hierarchy_white = cv2.findContours(White_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i, countor_0 in enumerate(Yellow_countors):
    if i == 0:
        continue
    epsilon_0 = 0.025 * cv2.arcLength(countor_0, True)
    approx_0 = cv2.approxPolyDP(countor_0, epsilon_0, True)

    cv2.drawContours(image, countor_0, 0, (45, 139, 87), 1)

    x, y, w, h = cv2.boundingRect(approx_0)

    x_mid = int(x + h/2)
    y_mid = int(y + h/2)

    coords = (x_mid, y_mid)
    color = (127,127,127)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx_0) == 3:
        cv2.putText(image,"Tam giac",coords, font, 0.5, color, 2)
    elif len(approx_0) == 7:
        cv2.putText(image, " Mui ten", coords, font, 0.5, color, 2)
    else :
        cv2.putText(image, "",coords, font, 0.5, color, 2)

#-------------------------------------------------------
for b, countor_1 in enumerate(Blue_countors):
    if b == 0:
        continue
    epsilon_1 = 0.03 * cv2.arcLength(countor_1, True)
    approx_1 = cv2.approxPolyDP(countor_1, epsilon_1, True)

    cv2.drawContours(image, countor_1, 0, (45, 139, 87), 1)

    x, y, w, h = cv2.boundingRect(approx_1)

    x_mid_1 = int(x + w/2)
    y_mid_1 = int(y + h/2)

    coords_new = (x_mid_1, y_mid_1)
    color = (127,127,127)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx_1) == 3:
        cv2.putText(image,"Tam giac",coords_new, font, 0.5, color, 2)
    elif len(approx_1) == 7:
        cv2.putText(image, " Mui ten", coords_new, font, 0.5, color, 2)
    else :
        cv2.putText(image, "",coords_new, font, 0.5, color, 2)

#-----------------------------------------
for g, countor_2 in enumerate(Green_countors):
    if g == 0:
        continue
    epsilon_2 = 0.025 * cv2.arcLength(countor_2, True)
    approx_2 = cv2.approxPolyDP(countor_2, epsilon_2, True)

    cv2.drawContours(image, countor_2, 0, (45, 139, 87), 1)

    x, y, w, h = cv2.boundingRect(approx_2)

    x_mid_2 = int(x + w/2)
    y_mid_2 = int(y + h/2)

    coords_new = (x_mid_2, y_mid_2)
    color = (127,127,127)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx_2) == 3:
        cv2.putText(image,"Tam giac",coords_new, font, 0.5, color, 2)
    elif len(approx_2) == 7:
        cv2.putText(image, " Mui ten", coords_new, font, 0.5, color, 2)
    else :
        cv2.putText(image, "",coords_new, font, 0.5, color, 2)

#-----------------------------------------------------
for p, countor_4 in enumerate(Pink_countors):
    if p == 0:
        continue
    epsilon_4 = 0.0245 * cv2.arcLength(countor_4, True)
    approx_4 = cv2.approxPolyDP(countor_4, epsilon_4, True)

    cv2.drawContours(image, countor_4, 0, (45, 139, 87), 1)

    x, y, w, h = cv2.boundingRect(approx_4)

    x_mid_4 = int(x + w/2)
    y_mid_4 = int(y + h/2)

    coords_new = (x_mid_4, y_mid_4)
    color = (127,127,127)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx_4) == 3:
        cv2.putText(image,"Tam giac",coords_new, font, 0.5, color, 2)
    elif len(approx_4) == 7:
        cv2.putText(image, " Mui ten", coords_new, font, 0.5, color, 2)
    else :
        cv2.putText(image, "",coords_new, font, 0.5, color, 2)

#----------------------------------------
for w1, countor_5 in enumerate(White_countors):
    if w1 == 0:
        continue
    epsilon_5 = 0.021 * cv2.arcLength(countor_5, True)
    approx_5 = cv2.approxPolyDP(countor_5, epsilon_5, True)

    cv2.drawContours(image, countor_5, 0, (45, 139, 87), 1)

    x, y, w, h = cv2.boundingRect(approx_5)

    x_mid = int(x + h/2)
    y_mid = int(y + h/2)

    coords = (x_mid, y_mid)
    color = (127,127,127)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if len(approx_5) == 3:
        cv2.putText(image,"Tam giac",coords, font, 0.5, color, 2)
    elif len(approx_5) == 7:
        cv2.putText(image, " Mui ten", coords, font, 0.5, color, 2)
    else :
        cv2.putText(image, "",coords, font, 0.5, color, 2)


# Nhan dang hinh dang + mau sac ( ngu giac + mau do )
hsv_0 = cv2.cvtColor(img_0, cv2.COLOR_BGR2HSV) # Doi hsv cho anh 1 de nhan dang mau
hsv_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV) # Doi hsv cho anh 1 de nhan dang mau
# Giu mau do muc duoi
Lower_red_0 = np.array([0,100,100])
Upper_red_0 = np.array([20,255,255])
# Giu mau do muc tren
Lower_red_1 = np.array([171,120,120])
Upper_red_1 = np.array([200,255,255])
# Tao mask loc mau do
Red_mask_0 = cv2.inRange(hsv_0, Lower_red_0,Upper_red_0)
Red_mask_1 = cv2.inRange(hsv_1, Lower_red_1, Upper_red_1)
# Ket qua
Red_0_Filter = cv2.bitwise_and(img_0, img_0, mask= Red_mask_0)
Red_1_Filter = cv2.bitwise_and(img_1, img_1, mask= Red_mask_1)
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
    color = (127,127,127)
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


cv2.waitKey(0)
cv2.destroyAllWindows()