# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 23:44:26 2022

@author: sachd
"""
import sqlite3

def display():
    connection = sqlite3.connect("Academic Record Manager_2.db")
  
    # cursor
    crsr = connection.cursor()
    ans=crsr.execute("SELECT Semester, Student.Scholar_number,First_name, Last_name, Mathematics, Science, English, Social_Science, Second_Language, Percentage from Student LEFT JOIN SubjectMarks ON Student.Scholar_number=SubjectMarks.Scholar_number order by Semester")
    for i in ans:
        print(i)
    connection.close()
#display()
    