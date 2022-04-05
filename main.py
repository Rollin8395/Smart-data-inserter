from openpyxl import load_workbook
from datetime import date
import requests
import os
from requests.auth import HTTPBasicAuth
import pypyodbc as odbc
import glob
import pandas as pd
from datetime import datetime
import time

now=datetime.now()
current_time = now.strftime("%H:%M:%S")






#get current date
def current_date(url):
    today = date.today()
    new_url = url.replace('TODAYDATE', str(today))
    return new_url

#download the file
def file_retrieve(username,password,link):
    basic=HTTPBasicAuth(username,password)
    q=requests.get(link,auth=basic)
    url_content=q.content
    csv_file = open ('downloaded.csv','wb')
    csv_file.write(url_content)
    csv_file.close()

#to rename file
def rename_file(name):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    file = name
    filename = "%s.csv" % file
    os.rename('downloaded.csv', filename)

    return name



# import csv files data into a dataframe
def csv_to_dataframes(path):
    filenames = glob.glob(path + "/*.csv")
    li = []
    for file in filenames:
        df = pd.read_csv(file, index_col=None, header=0)
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)


def data_frame_add_column_ip(csvfile,name):
    data=pd.read_csv(csvfile)
    df=pd.DataFrame(data)
    df['Camera name']=name
    return df





