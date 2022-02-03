# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 00:22:33 2022

@author: sachd
"""
import sqlite3

def initialize():
    connection = sqlite3.connect("Academic Record Manager_2.db")
  
    # cursor
    crsr = connection.cursor()
    #crsr.execute('''DROP TABLE Student;''')
    #connection.commit()
    # SQL command to create a table in the database
    '''sql_command = """CREATE TABLE Student ( 
    Scholar_number INTEGER PRIMARY KEY, 
    First_name VARCHAR(20), 
    Last_name VARCHAR(30), 
    gender CHAR(1), 
    joining DATE,
    Semester INTEGER,
    Percentage DOUBLE);"""
    
    crsr.execute(sql_command)
    
    sql_command = """INSERT INTO Student VALUES (1642, "Rishabh",\
    "Bansal", "M", "2014-03-28", 5, 95);"""
    crsr.execute(sql_command)
      
    # another SQL command to insert the data in the table
    sql_command = """INSERT INTO Student VALUES (5421, "Bill", "Gates",\
    "M", "1980-10-28",7, 81);"""
    crsr.execute(sql_command)
    connection.commit() '''
    crsr.execute("DROP Table SubjectMarks")
    sql_command = """CREATE TABLE SubjectMarks ( 
    Scholar_number INTEGER PRIMARY KEY, 
    Mathematics DOUBLE,
    Science DOUBLE,
    English DOUBLE,
    Social_Science DOUBLE,
    Second_Language DOUBLE);"""
    
    crsr.execute(sql_command)
    
    sql_command = """INSERT INTO SubjectMarks VALUES (1221,80,80,75,70,70);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO SubjectMarks VALUES (1234,60,60,55,50,50);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO SubjectMarks VALUES (1642,100,100,95,90,90);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO SubjectMarks VALUES (5421,83,83,71,79,79);"""
    crsr.execute(sql_command)
    
    ans=crsr.execute("SELECT * FROM SubjectMarks")
    for i in ans:
        print(i)
    connection.commit()
    connection.close()
    # execute the statement
    #crsr.execute(sql_command)
initialize()
# close the connect
    