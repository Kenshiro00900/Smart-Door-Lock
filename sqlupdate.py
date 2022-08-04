"""
Created on Sunday Nov 13 2019
@author: Neeraj

"""
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import sqlite3
import pyfingerprint
import hashlib
import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

global str


def Unlock():
    print('welcome')
    GPIO.output(18, GPIO.HIGH)

    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
def update():
            try:
                  print("enter the row for update")
                  print("1. roll num")
                  print("2. name")
                  print("3. finger print")
                  print("4. books")
                  
                  r=int(input("enter college id ="))
                  n=input("enter name of student=")
                  b=input("class roll number =")
                  conn = sqlite3.connect('library_database.db')
                  curs= conn.cursor()
                  print("Connected to SQLite")
                  curs.execute  ('''UPDATE student_table SET name = ?,college_rollnum = ?  WHERE college_id= ? ''', (n,b,r)) 
                  print("just end")
                  conn.commit()
                  print("Record Updated successfully ")
                  curs.close()


            except Exception as e:
                     print('Operation failed!')
                     print('Exception message: ' + str(e))
                    


def delete():
            try:
                  print("enter the roll number of student for delete info.")
                  r=input("enter college id =")
                  conn = sqlite3.connect('library_database.db')
                  curs= conn.cursor()
                  print("Connected to SQLite")
                  curs.execute('''DELETE FROM student_table WHERE college_id = ?''',(r, ))
                  conn.commit()
                  print("Record Updated successfully ")
                  curs.close()
                  
            except Exception as e:
                     print('Operation failed!')
                     print('Exception message: ' + str(e))



def select():
                
               def allinfo():
                         try:
                                print(" all student info. from database ")
                                conn = sqlite3.connect('library_database.db')
                                curs= conn.cursor()
                                print("Connected to SQLite")
                                curs.execute('''SELECT * FROM student_table''')
                                records = curs.fetchall()
                                print("total rows are: ", len(records))
                                for row in records:
                                    print("\n*******************************************************************\n")
                                    print("college id: ",row[0])
                                    print("name    : ",row[1])
                                    print("batch: ",row[2])
                                    print("department: ",row[3])
                                    print("fingerprint: ",row[4])
                                    print("position: ",row[5])
                                    print("\n*******************************************************************\n")


                         except Exception as e:
                                    print('Operation failed!')
                                    print('Exception message: ' + str(e))

               allinfo()

                      
            
