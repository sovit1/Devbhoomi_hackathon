import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd
import numpy as np
import pywhatkit
import datetime

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)

client = gspread.authorize(creds)

sheet = client.open("hello_world").sheet1  # Open the spreadsheet

data = sheet.get_all_records()

data_df = pd.DataFrame.from_dict(data)

data_df.head()
target=data_df['Target Plate'].iloc[0]
target_df=data_df[data_df['Plate']==target]
print(target_df['Phone'].iloc[0])
b=target_df['Phone'].iloc[0]
s=target_df['Name'].iloc[0]
s=str(s)
c=str(b)

sheet.update_cell(2,5,c)#updating OUTPUT
#Speed reading from sheet
m=data_df['Speed'].iloc[0]
d="+91"+c
time=datetime.datetime.now()
hour=time.hour
minute=time.minute+2
if(m>25): #checking speed limit
    pywhatkit.sendwhatmsg(d, 'Hey! ' + s + ' We observed you are overspeeding\nYour speed : ' + str(m) + 'km/hr\nPlease pay fine of Rs.2000', hour, minute)



