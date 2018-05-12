from __future__ import print_function
from getpass import unix_getpass

import io
import mysql.connector

dicarg={}

dicarg['user']=input('Please input the user name: ')
dicarg['password']=unix_getpass('Please input the password: ')
dicarg['database']=input('Please input the database you want: ')

cnx=mysql.connector.connect(**dicarg)
cursor=cnx.cursor()

def AbstractValues(filepath,data):
	b=("(",",",")","'")
	f_stream=open(filepath)
	while 1:
		line=f_stream.readline()
		if line!='':
			LineList=[]
			for i in range(0,len(line)-1):
				if line[i] in b:
					for j in range(i+1,len(line)-1):
						if line[j] in b:
							if j!=i+1:
								LineList.append(line[i+1:j])
							i=j
							break
			LineTuple=tuple(LineList)
			data.append(LineTuple)
		else :
			f_stream.close()
			break



table=input('Please input the table name you want to insert values: ')
add_table=("insert into {} values (%s,%s)".format(table))

filepath=input('Please input the file: ')
data=[]
AbstractValues(filepath,data)

cursor.executemany(add_table,data)

cnx.commit()

cursor.close()
cnx.close()
