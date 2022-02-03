# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 23:02:45 2022

@author: sachd
"""
import sqlite3
#import mysql.connector

def delete(sch_no):
    #print(type(sch_no))
    connection = sqlite3.connect("Academic Record Manager_2.db")
    crsr = connection.cursor()
    crsr.execute("DELETE from Student where Scholar_number=?",(sch_no,))
    connection.commit()    
    connection.close()
#delete(1212)