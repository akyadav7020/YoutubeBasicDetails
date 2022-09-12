import pyodbc

def connection():
    try:
        mydb = pyodbc.connect(
            'DRIVER={SQL Server};''SERVER=mydb708.database.windows.net;''DATABASE=my_DB1;''UID=root708;''PWD=root@123')
        cursor = mydb.cursor()
        return cursor,mydb
    except Exception as e:
        return "Not able to connect to the SERVER"

def insert_unique_data(primary_column,table,data):
    try:
        cursor,mydb = connection()
        cursor.execute("select {} from {}".format(primary_column,table))
        all_values_in_primary_column = (cursor.fetchall())
        all_values_list = set()
        for i in range(len(all_values_in_primary_column)):
            all_values_list.add(all_values_in_primary_column[i][0])
        input_value = data[list(data.keys())[0]]

        if input_value not in all_values_list:
            cursor.execute("insert into {} values('{}','{}','{}','{}','{}')".format(table,data['V_link'],data['Likes'],data['Title'],data['thumbnail'],data['Views']))
            mydb.commit()
        else:
            Update_Data(primary_column,table,data)
    except Exception as e:
        return "Not able to connect to the SERVER"


def create_unique_table(input_table_name):
    try:
        cursor,mydb = connection()
        cursor.execute("select table_name from information_schema.tables")
        all_tables_name = (cursor.fetchall())
        all_tables_list = set()
        for i in range(len(all_tables_name)):
            all_tables_list.add(all_tables_name[i][0])

        if input_table_name not in all_tables_list:
            cursor.execute("create table {}(video_link varchar(100),likes int,title varchar(500), thumbnail_url varchar(100),views int)".format(input_table_name))
            mydb.commit()
    except Exception as e:
        return "Not able to connect to the SERVER"

def Update_Data(primary_column,table,data):
    try:
        cursor,mydb = connection()
        cursor.execute("update {} set likes = {}, views={} where {} = '{}'".format(table,data['Likes'],data['Views'],primary_column,data['V_link']))
        mydb.commit()

    except Exception as e:
        return "Not able to connect to the SERVER"

def Extract_data():
    try:
        cursor,mydb = connection()
        cursor.execute("select table_name from information_schema.tables")
        all_tables_name = (cursor.fetchall())
        all_tables_list = []
        for i in range(len(all_tables_name)-1):
            all_tables_list.append(all_tables_name[i][0])
        records=[]
        for i in range (len(all_tables_list)):
            cursor.execute("select video_link from {}".format(all_tables_list[i]))
            all_data = (cursor.fetchall())
            mydict = {"Ch_table": all_tables_list[i], "records": len(all_data)}
            records.append(mydict)
        return records
    except Exception as e:
        return "No records Found"

