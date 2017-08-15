import os.path
import os,time
from pathlib import Path
import pandas
import datetime as dt
from sqlalchemy import *
time.ctime()
db = create_engine('mysql://root:toor@localhost/client')#database address, you can change it
meta = MetaData(db)
table1 = Table('DataSensor1', meta, #table name, you can change it
   Column('id',Integer,primary_key=True),
   Column('Jenis_sensor', String(50)),
   Column('Tipe_sensor', String(50)),
   Column('Value', Integer),
   Column('Tanggal', Date),
   Column('Ket', String(50)))
table2 = Table('DataSensor2', meta,
   Column('id',Integer,primary_key=True),
   Column('Jenis_sensor', String(50)),
   Column('Tipe_sensor', String(50)),
   Column('Value', Integer),
   Column('Tanggal', Date),
   Column('Ket', String(50)))
table3 = Table('DataSensor3', meta,
   Column('id',Integer,primary_key=True),
   Column('Jenis_sensor', String(50)),
   Column('Tipe_sensor', String(50)),
   Column('Value', Integer),
   Column('Tanggal', Date),
   Column('Ket', String(50)))

##table3.create()
#with open('sensortest.txt') as csvfile:
#     tbl_reader = csv.reader(csvfile, delimiter=',')
#     for row in tbl_reader:
#       table.insert().values(id=row[0], Tanggal=row[1], Tipe_sensor=row[2], Value=row[3], Ket=row[4])
file_name1 = Path('sensortest1.txt')#file path and filename, you can change it
file_name2 = Path('sensortest2.txt')
file_name3 = Path('sensortest3.txt')
i=1
while (i==1):
	if file_name1.is_file():
		df1 = pandas.read_sql(select([table1]), db,)
		df_file1 = pandas.read_csv(file_name1,sep=',',header=None,names=df1)
		df_file1.to_sql(con=db, index=False,name='DataSensor1',if_exists='append')
		print (time.strftime('%H:%M:%S  Data sensor1 has been inputed'))
		print df_file1
		time.sleep(5)
		os.remove('sensortest1.txt')
	else:
		print (time.strftime('%H:%M:%S  Data sensor1 not found'))

	if file_name2.is_file():
		df2 = pandas.read_sql(select([table2]), db,)
		df_file2 = pandas.read_csv(file_name2,sep=',',header=None,names=df2)
		df_file2.to_sql(con=db, index=False,name='DataSensor2',if_exists='append')
		print (time.strftime('%H:%M:%S Data sensor2 has been inputed'))
		print df_file2
		time.sleep(5)
		os.remove('sensortest2.txt')
	else: 
		print (time.strftime('%H:%M:%S  Data sensor2 not found'))

	if file_name3.is_file():
		df3 = pandas.read_sql(select([table3]), db,)
		df_file3 = pandas.read_csv(file_name3,sep=',',header=None,names=df3)
		df_file3.to_sql(con=db, index=False,name='DataSensor3',if_exists='append')
		print (time.strftime('%H:%M:%S  Data sensor3 has been inputed'))
		print df_file3
		time.sleep(5)
		os.remove('sensortest3.txt')
	else:
		print (time.strftime('%H:%M:%S  Data sensor3 not found'))
