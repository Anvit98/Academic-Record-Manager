# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:21:42 2022

@author: sachd
"""

import sqlite3

def categorize():
    connection = sqlite3.connect("Academic Record Manager_2.db")
  
    # cursor
    crsr = connection.cursor()
    sql_command = """SELECT *, CASE WHEN Percentage>=75 Then 'First Division and Distinction' WHEN Percentage>=60 AND Percentage<75 Then 'First Division' WHEN Percentage>=50 AND Percentage<60 Then 'Second Division' ELSE 'Fail' END AS DIVISION FROM Student;"""
    
    ans=crsr.execute(sql_command)
    #ans=crsr.execute("SELECT First_name FROM Student")
    for i in ans:
        print(i)
    connection.close()
#categorize()