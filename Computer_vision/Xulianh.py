import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
image = cv2.imread('F:/Veronica.jpg')
fig, ax = plt.subplots(1,2)

# Tạo một bản sao của ảnh để thực hiện phép toán giảm độ mờ
blurred_image = cv2.GaussianBlur(image, (0, 0), 3)

# Tính toán phép toán giảm độ mờ
sharpened_image = cv2.addWeighted(image, 1.5, blurred_image, -0.5, 0)
# Chuyển đổi
image_rgb_1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_rgb_2 = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)


# Hiển thị ảnh gốc và ảnh đã được làm sắc nét với cường độ sáng được giữ nguyên
#cv2.imshow('Original Image', image)
#cv2.imshow('Sharpened Image with Brightness Preserved', sharpened_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

ax[0].imshow(image_rgb_1)
ax[0].axis("off")

ax[1].imshow(image_rgb_2)
ax[1].axis("off")

# plt.plot(h1, color='blue', label='Image 1')
# plt.plot(h2, color='red', label='Image 2')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')
# plt.legend()
plt.show()
