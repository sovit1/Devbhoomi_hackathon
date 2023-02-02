import serial
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)
#
client = gspread.authorize(creds)
#
sheet = client.open("hello_world").sheet1  # Open the spreadsheet
#
data = sheet.get_all_records()

data_df = pd.DataFrame.from_dict(data)

data_df.head()
num=data_df['Speed'].iloc[0]
print(num)

arduino = serial.Serial(port='COM9', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    if(int(num) >=25): # Taking input from user
        value = write_read('1')
    else:
        value = write_read('0')


    print(value)
