# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:57:51 2022

@author: sachd
"""
import sqlite3

def sort(field,order):
    try:
        connection = sqlite3.connect("Academic Record Manager_2.db")
      
        # cursor
        crsr = connection.cursor()
        #sql_command = """SELECT * FROM Student order by (%s,%s);"""
        #print((field,order))
        if field=='a':
            if order=='asc':
                ans=crsr.execute("SELECT * FROM Student order by Scholar_number ASC")
            else:
                ans=crsr.execute("SELECT * FROM Student order by Scholar_number DESC")
        elif field=='b':
            if order=='asc':
                ans=crsr.execute("SELECT * FROM Student order by First_name ASC")
            else:
                ans=crsr.execute("SELECT * FROM Student order by First_name DESC")
        elif field=='c':
            if order=='asc':
                ans=crsr.execute("SELECT * FROM Student order by Last_name ASC")
            else:
                ans=crsr.execute("SELECT * FROM Student order by Last_name DESC")
        elif field=='d':
            if order=='asc':
                ans=crsr.execute("SELECT * FROM Student order by Percentage ASC")
            else:
                ans=crsr.execute("SELECT * FROM Student order by Percentage DESC")
        elif field=='e':
            if order=='asc':
                ans=crsr.execute("SELECT * FROM Student order by joining ASC")
            else:
                ans=crsr.execute("SELECT * FROM Student order by joining DESC")
        #ans=crsr.execute(sql_command)
        #ans=crsr.execute("SELECT First_name FROM Student")
        for i in ans:
            print(i)
        connection.close()
    except:
        print("Invalid Input")
#sort("f","desc")
    