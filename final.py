from main import *
os.remove('new.csv')
wb = load_workbook('ipaddress.xlsx')
ws = wb.active
column_b = ws['B']

while True:
    for cell in column_b:
        if cell.value == 'IP address':
            print()
        else:
            a = cell.value
            vari = 'http://IPADDRESS/dataloader.cgi?dw=logcsv&maintype=0&subtype=10&starttime=TODAYDATE-00:00:00&endtime=TODAYDATE-23:59:59'
            change_ip = vari.replace('IPADDRESS', a)
            url = change_ip  # replace with ip address got from excel sheet
            link = current_date(url)  # function for changing date in url
            print(link)
            file_retrieve('admin', 'P@55word', link)  # download file logs
            rename_file('new')  # rename the file
            filename = 'new' + '.csv'
            df = pd.read_csv(filename)
            for i in range(len(df)):
                Time = df['Time'][i]
                Sub = df[' Sub Type'][i]
                Param = df[' Param'][i]
                User = df[' User'][i]
                IP = df[' IP'][i]
                Detail = df[' Detail'][i]
                Main = df[' Main Type'][i]
                Name = a

                DRIVER = 'SQL Server'
                SERVER_NAME = 'DESKTOP-UJCVRU3'
                DATABASE_NAME = 'sparshptz'


                def connection_string(driver, server_name, database_name):
                    conn_string = f"""
                         DRIVER={{{driver}}};
                         SERVER={server_name};
                         DATABASE={database_name};
                       """
                    return conn_string


                conn = odbc.connect(connection_string(DRIVER, SERVER_NAME, DATABASE_NAME))
                cursor = conn.cursor()
                sql = "SELECT * from data_table_log WHERE Date_Time='" + str(Time) + "'"
                cursor.execute(sql)
                data = cursor.fetchone()
                sql1 = "SELECT * from data_table_log WHERE Main_Type='" + str(Main) + "'"
                cursor.execute(sql1)
                data1 = cursor.fetchone()
                sql2 = "SELECT * from data_table_log WHERE Sub_Type='" + str(Sub) + "'"
                cursor.execute(sql2)
                data2 = cursor.fetchone()

                if data is None:
                    cursor = conn.cursor()
                    sql = (
                        "INSERT INTO  data_table_log(Date_Time,Main_Type,Sub_Type,Param_,User_,IP_,Detail,Camera_name) VALUES(?,?,?,?,?,?,?,?)")

                    val = (Time, Main, Sub, Param, User, IP, Detail, Name)
                    cursor.execute(sql, val)
                    print(val, 'New data added')
                    conn.commit()


                else:
                    pass

                if data1 is None:
                    cursor = conn.cursor()
                    sql = (
                        "INSERT INTO  data_table_log(Date_Time,Main_Type,Sub_Type,Param_,User_,IP_,Detail,Camera_name) VALUES(?,?,?,?,?,?,?,?)")

                    val = (Time, Main, Sub, Param, User, IP, Detail, Name)
                    cursor.execute(sql, val)
                    print(val, 'New data added')
                    conn.commit()


                else:
                    pass

                if data2 is None:
                    cursor = conn.cursor()

                    sql = (
                        "INSERT INTO  data_table_log(Date_Time,Main_Type,Sub_Type,Param_,User_,IP_,Detail,Camera_name) VALUES(?,?,?,?,?,?,?,?)")

                    val = (Time, Main, Sub, Param, User, IP, Detail, Name)
                    cursor.execute(sql, val)
                    print(val, 'New data added')
                    conn.commit()


                else:
                    pass
                cursor.close()
                conn.close()
            time.sleep(10)
            os.remove(filename)
