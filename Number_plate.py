import cv2
import matplotlib.pyplot as plt
lic_data=cv2.CascadeClassifier('C:\\Users\\Administrator\\Downloads\\haarcascade_russian_plate_number.xml')
def plt_show(image,title="",gray=False,size=(100,100)):
    temp=image
    if gray== False:
        temp=cv2.cvtColor(temp,cv2.COLOR_BGR2RGB)
        plt.title(title)
        plt.imshow(temp,cmap='gray')
        plt.show()

def detect_numnber(img):
    temp=img
    gray=cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
    number=lic_data.detectMultiscale(img,1.2)
    print("Number plate detected"+str(len(number)))
    for numbers in number:
        (x,y,w,h)=numbers
        roi_gray=gray[y:y+h, x:x+w]
        roi_color= img[y:y+h,x:x+h]
        cv2.rectangle(temp,(x,y),(x+w,y+h),(0,255,0),3)

    plt_show(temp)

    img=cv2.imread("car.png")
    plt_show(img)
    detect


