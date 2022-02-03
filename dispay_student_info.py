# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:06:14 2022

@author: sachd
"""
import sqlite3

def display():
    connection = sqlite3.connect("Academic Record Manager_2.db")
  
    # cursor
    crsr = connection.cursor()
    ans=crsr.execute("SELECT * FROM Student")
    #print("hi")
    for i in ans:
        print(i)
    connection.close()
#display()
    