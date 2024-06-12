import cv2
import matplotlib.pyplot as plt


image = cv2.imread("F:/Veronica.jpg")
#Cong thuc tinh toan
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray,threshold1=60,threshold2=225)
inverted_image = cv2.bitwise_not(image)
#Histogram
histogram_b = cv2.calcHist([image],[0],None,[256],[0,256])
histogram_g = cv2.calcHist([image],[1],None,[256],[0,256])
histogram_r = cv2.calcHist([image],[2],None,[256],[0,256])

#In ra ket qua
#Anh goc
cv2.imshow("Original Image",image)
#Anh xam
cv2.imshow("Black_White_Image",gray)
#Tach nen
cv2.imshow("Tach nen",edge)
#Nghich dao
cv2.imshow("Nghich dao",inverted_image)
#Histogram
plt.plot(histogram_b, color ='blue')
plt.plot(histogram_g, color = 'green')
plt.plot(histogram_r, color = 'red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Histogram')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()