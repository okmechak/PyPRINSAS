#!/usr/bin/python
import pyodbc
import MySQLdb

#Access database engine should be installed!! TODO add this nnote to documentation
x = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]

print(x)

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\ofcra\Google Drive\Study\PyPRINSAS\PRINSAS Data\SANSRAW.mdb;'
    )
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\ofcra\Dev\pyprinsas\data\sample\SANSRaw.mdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
for table_info in crsr.tables(tableType='TABLE'):
    print(table_info.table_name)
