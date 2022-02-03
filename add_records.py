# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:04:30 2022

@author: sachd
"""

import sqlite3
from datetime import datetime

def add(n):
    connection = sqlite3.connect("Academic Record Manager_2.db")
    crsr = connection.cursor()
    for i in range(n):
        print("Stuent No.: ",(i+1))
        scholar_no=int(input("Enter scholar number of the student: "))
        first_name=input("Enter first name of the student: ")
        last_name=input("Enter last name of the student: ")
        gender=input("Enter gender of the student (M/F): ")
        #first_name=input("Enter first name of the student: ")
        doj_string=input("Enter date of joining of the student in the format YYYY-MM-DD: ")
        doj = datetime.strptime(doj_string, '%Y-%m-%d')
        class_name=int(input("Enter class of the student: "))
        percent=float(input("Enter percentage of the student: "))
        #sql_command = """INSERT INTO Student VALUES (%d,%s,%s,%c,%Y-%m-%d,%d,%f);"""
        crsr.execute("INSERT INTO Student VALUES (?,?,?,?,?,?,?)", (scholar_no,first_name,last_name,gender,doj,class_name,percent))
        connection.commit()
    connection.close()
#add(1)
        
        
        