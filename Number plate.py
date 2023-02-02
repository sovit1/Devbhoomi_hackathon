import aiocv
import cv2
img = cv2.imread('C:\\Users\\Administrator\\Desktop\\Cyborg\\numberplate_car.jpeg')
# Make An Object
car = aiocv.NumberPlateDetector(img)
# Use findNumberPlate() Method To Detect Number Plate On Image/Video
car.findNumberPlate()
cv2.imshow("Image",img)
cv2.waitKey(0)