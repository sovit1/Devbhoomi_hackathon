import cv2
import time
import matplotlib.pyplot as plt
import requests
import numpy as np
import imutils
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd
import numpy as np
import pywhatkit
import datetime

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)
#
client = gspread.authorize(creds)
#
sheet = client.open("hello_world").sheet1  # Open the spreadsheet
#



# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
#url = "http://192.168.137.162:8080/shot.jpg"
cap = cv2.VideoCapture('C:\\Users\\Administrator\\Downloads\\car-video_0.5x.mp4')  #Path to footage

car_cascade = cv2.CascadeClassifier('C:\\Users\\Administrator\\Desktop\\Cyborg\\cars.xml')  #Path to cars.xml


#Coordinates of polygon in frame::: [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
coord=[[239,20],[265,20],[239,300],[265,300]]

#Distance between two horizontal lines in (meter)
scaling_factor=3/40
dist = scaling_factor*(coord[1][0]-coord[0][0])
c=0
e=0

while True:
    ret, img = cap.read()
   # img_resp = requests.get(url)
    #img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    #img = cv2.imdecode(img_arr, -1)
    #img = imutils.resize(img, width=1920, height=1080)
    #cv2.imshow("Android_cam", img)



    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(img,1.8,2)


    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)


    cv2.line(img, (coord[0][0],coord[0][1]),(coord[1][0],coord[1][1]),(0,0,255),2)   #First horizontal line
    cv2.line(img, (coord[0][0],coord[0][1]), (coord[2][0],coord[2][1]), (0, 0, 255), 2) #Vertical left line
    cv2.line(img, (coord[2][0],coord[2][1]), (coord[3][0], coord[3][1]), (0, 0, 255), 2) #Second horizontal line
    cv2.line(img, (coord[1][0],coord[1][1]), (coord[3][0], coord[3][1]), (0, 0, 255), 2) #Vertical right line

    for (x, y, w, h) in cars:
        if(x==coord[2][0]):
            cv2.line(img, (coord[0][0],coord[0][1]), (coord[2][0], coord[2][1]), (0, 255,0), 2) #Changes line color to green

            tim1= time.time() #Initial time
            print("Car Entered.")
            e=1

        if (x==coord[1][0]):
            cv2.line(img, (coord[1][0], coord[1][1]), (coord[3][0], coord[3][1]), (0, 0, 255), 2)#Changes line color to green
            tim2 = time.time() #Final time
            print("Car Left.")
            #We know that distance is 3cm
            s=(dist / ((tim2 - tim1))) * 4
            print("Speed in (cm/s) is:",s )
            sheet.update_cell(2,7,s)
            c=-1
            break

    if(c==-1):
        break
    cv2.imshow('img',img) #Shows the frame



    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()