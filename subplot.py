import cv2
import matplotlib.pyplot as plt

image = cv2.imread('F:/Veronica.jpg')
#fig, ax = plt.subplots(2,2)

# Tạo một bản sao của ảnh để thực hiện phép toán giảm độ mờ
#blurred_image = cv2.GaussianBlur(image, (0, 0), 3)
# Tính toán phép toán giảm độ mờ
#sharpened_image = cv2.addWeighted(image, 1.5, blurred_image, -0.5, 0)
# Chuyển đổi
#image_rgb_1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#image_rgb_2 = cv2.cvtColor(sharpened_image, cv2.COLORc_BGR2RGB)

#Sac net
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(image, cv2.CV_64F)

laplacian = cv2.convertScaleAbs(laplacian)

sharpened_image = cv2.addWeighted(image, 1.0, laplacian, 0, 0)

# ax[0,0].imshow(image)
# ax[0,0].axis("off")
# ax[0,1].imshow(sharpened_image)
# ax[0,1].axis("off")
# ax[1,0].imshow(image_rgb_1)
# ax[1,0].axis("off")
# ax[1,1].imshow(image_rgb_2)
# ax[1,1].axis("off")
#plt.show()

cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



