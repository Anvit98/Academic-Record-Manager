# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 00:06:26 2022

@author: sachd
"""

import sqlite3
#import initialize_data
import dispay_student_info
import division_category
import sort_data
import add_records
import update_data
import delete_record
import display_subject_marks

def start():
    #initialize_data.initialize()
    while(True):
        print("        Welcome to the Academic Record Manager     ")
        print("------------------------------------------------------")
        print("Enter 1. To Display all Student's Information")
        print("Enter 2. To Add New Records in the databse")
        print("Enter 3. To Sort the Student's Data according to your field of choice")
        print("Enter 4. To Categorize the Students into their Divison Percentage")
        print("Enter 5. To Update the records")
        print("Enter 6. To Delete a record")
        print("Enter 7. To Display information about the marks obtained by students in various subjects")
        print("Enter 8. To Exit ")
        try:
            a=int(input("Select a choice from 1-8: "))
            if a==1:
                print("\n")
                print("The information is dispayed in the following format:-")
                print("\n")
                print("(Scholar_number, First_name, Last_name, Gender, Joining_date, Class, Percentage)")
                print("\n")
                print("The records in the database are:-")
                print("\n")
                dispay_student_info.display()
                print("\n")
            elif a==2:
                print("\n")
                n=int(input("Please enter the no. of records you would like to enter in the database: "))
                add_records.add(n)
            elif a==3:
                print("\n")
                print("This operation will sort the academic data as per your field of choice")
                print("\n")
                print("Enter a. To Sort the data according to Scholar_number of the students")
                print("Enter b. To Sort the data according to First_name of the students")
                print("Enter c. To Sort the data according to Last_name of the students")
                print("Enter d. To Sort the data according to Percentage of the students")
                print("Enter e. To Sort the data according to Joining_date of the students")
                print("\n")
                field=input("Select a choice from a-e: ")
                print("\n")
                print("Enter asc. To Sort the data as per your chosen field in Ascending order")
                print("Enter desc. To Sort the data as per your chosen field in Desscending order")
                print("\n")
                order=input("Select either asc or desc: ")
                print("\n")
                print("The information is dispayed in the following format:-")
                print("\n")
                print("(Scholar_number, First_name, Last_name, Gender, Joining_date, Class, Percentage, Division)")
                print("\n") 
                sort_data.sort(field,order)
                print("\n")
            elif a==4:
                print("\n")
                print("The students are categorized into division according to their percentage as follows:-")
                print("\n")
                print("First Division and Distinction: 75% and above")
                print("First Division: 60% - 75%")
                print("Second Division: 50% - 60%")
                print("Fail: Below 50%")
                print("\n")
                print("The information is dispayed in the following format:-")
                print("\n")
                print("(Scholar_number, First_name, Last_name, Gender, Joining_date, Class, Percentage, Division)")
                print("\n")  
                division_category.categorize()
                print("\n")
            elif a==5:
                print("\n")
                sch_no=int(input("Enter scholar number of the student whose record you would like to update: "))
                field=input("Enter a particular field name which you would like to update (Valid choices- 'First_name','Last_name','Class','Percentage'): ")
                value=input("Enter updated value of the field: ")
                update_data.update(sch_no,field,value)
                print("Entry has been updated")
                print("\n")
                #print("Enter scholar number of the student whose record you would like to update: ")
            elif a==6:
                print("\n")
                sch_no=int(input("Enter scholar number of the student whose record you would like to delete from the database: "))
                #print(sch_no)
                delete_record.delete(sch_no)
                print("Entry has been deleted")
                print("\n")
            elif a==7:
                print("\n")
                print("This operation gives the data about the marks obtained by all the students in various subjects (subjects include Mathematics, Science, English, Social Studies, Second Language). The students are grouped as per their respective classes.")
                print("The information is dispayed in the following format:-")
                #print("\n")
                print("(Class, Scholar_number, First_name, Last_name, Mathematics, Science, English, Social Science, Second Language, Percentage)")
                print("\n") 
                display_subject_marks.display()
                print("\n") 
            elif a==8:
                print("Thank you for using the Academic Record Manager")
                break
            else:
                print("Please enter a valid choice from 1-8")
        except ValueError:
            print("Please enter input as suggested.")
start()
        
'''connection = sqlite3.connect("Academic Record Manager.db")
  
# cursor
crsr = connection.cursor()
  
# print statement will execute if there
# are no errors
print("Connected to the database")

#crsr = connection.cursor()
  
# execute the command to fetch all the data from the table emp
#crsr.execute("SELECT * FROM emp")
  
# store all the fetched data in the ans variable
#ans = crsr.fetchall()
  
# Since we have already selected all the data entries
# using the "SELECT *" SQL command and stored them in
# the ans variable, all we need to do now is to print
# out the ans variable
#for i in ans:
#    print(i)
  
# close the connection
connection.close()'''