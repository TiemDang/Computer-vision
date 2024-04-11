import cv2
import numpy as np

# Tạo một hình ảnh màu đen với kích thước 400x300 pixels
image = np.zeros((580, 580, 3), dtype="uint8") * 255
image_test = np.zeros((1000,1000,3),dtype="uint8") * 255


# Hinh tron to bao quanh
center_1 = (240, 240)
radius_1 =  240
color_1 = (255,255,255)
thickness_1 = 1
# Hinh tron nho xung quanh
#1 Vi tri tren
center_2 = (240,80)
radius_2 = 80
color_2 = (255,255,255)
#2 Vi tri duoi
center_3 = (240,400)
#3 Vi tri trai tren
center_4 = (101,160)
#4 Vi tri trai duoi
center_5 = (101,320)
#5 Vi tri phai tren
center_6 = (379,160)
#6 Vi tri phai duoi
center_7 = (379,320)

#Hinh tam giac

TG_1 = np.array([[240,80],[101,320],[379,320]],np.int32)
TG_1 = TG_1.reshape(-1,1,2)
TG_2 = np.array([[240,400],[101,160],[379,160]],np.int32)
TG_2 = TG_2.reshape(-1,1,2)

# Hinh tu giac ben trong

color_3 = (255,0,0)

#Ve hinh

cv2.circle(image,center_1,radius_1,color_1,thickness_1)
cv2.circle(image,center_2,radius_2,color_2,thickness_1)
cv2.circle(image,center_3,radius_2,color_2,thickness_1)
cv2.circle(image,center_4,radius_2,color_2,thickness_1)
cv2.circle(image,center_5,radius_2,color_2,thickness_1)
cv2.circle(image,center_6,radius_2,color_2,thickness_1)
cv2.circle(image,center_7,radius_2,color_2,thickness_1)
cv2.polylines(image,[TG_1],True,(0,0,255),thickness_1)
cv2.polylines(image,[TG_2],True,(0,0,255),thickness_1)
cv2.line(image,center_2,center_4,color_3,thickness_1)
cv2.line(image,center_2,center_6,color_3,thickness_1)
cv2.line(image,center_4,center_5,color_3,thickness_1)
cv2.line(image,center_6,center_7,color_3,thickness_1)
cv2.line(image,center_5,center_3,color_3,thickness_1)
cv2.line(image,center_7,center_3,color_3,thickness_1)
cv2.line(image,center_1,center_2,color_3,thickness_1)
cv2.line(image,center_1,center_5,color_3,thickness_1)
cv2.line(image,center_1,center_7,color_3,thickness_1)

# Camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
# Tao cua so camera
cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Camera",(600,400))
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    color_4 = (0, 255, 0)
    thickness_2 = 3
    text = "Dang The Tiem"
    start_point_image = (250, 530)
    start_point_frame = (270, 350)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # Màu trắng, định dạng BGR
    thickness = 2
    frame = cv2.resize(frame,(600,400))
    new_frame = cv2.rectangle(frame,(250,150),(350,250),color_4,thickness_2)
    cv2.putText(new_frame, text, start_point_frame, font, font_scale, color, thickness)
    cv2.imshow('frame', new_frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.resize(frame,(600,400))
# Ve hinh vuong vao tam anh tu camera
color_4 = (0,255,0)
thickness_2 = 3
cv2.rectangle(frame,(250,150),(350,250),color_4,thickness_2)

# Ten
text ="Dang The Tiem"
start_point_image = (250,530)
start_point_frame = (270,350)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)  # Màu trắng, định dạng BGR
thickness = 2
cv2.putText(image, text, start_point_image, font, font_scale, color, thickness)
cv2.putText(frame, text, start_point_frame, font, font_scale, color, thickness)


#Hiển thị hình ảnh + video
cv2.imshow("Line", image)
cv2.imshow("Camera", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
