# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:58:13 2022

@author: sachd
"""
import sqlite3

def update(sch_no,field,value):
    connection = sqlite3.connect("Academic Record Manager_2.db")
    crsr = connection.cursor()
    if field=="First_name":
        crsr.execute("Update Student set First_name=? where Scholar_number=?",(value,sch_no))
        connection.commit()
    elif field=="Last_name":
        crsr.execute("Update Student set Last_name=? where Scholar_number=?",(value,sch_no))
        connection.commit()        
    elif field=="Class":
        crsr.execute("Update Student set Semester=? where Scholar_number=?",(int(value),sch_no))
        connection.commit()  
    elif field=="Percentage":
        crsr.execute("Update Student set Percentage=? where Scholar_number=?",(float(value),sch_no))
        connection.commit() 
    else:
        print("Invalid Value")
    connection.close()
#update(1212,"Class","6")