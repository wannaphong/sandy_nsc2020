# -*- coding: utf-8 -*-
import mysql.connector 
import pyodbc
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="diary") #Connect to data base 

mycursor = mydb.cursor() 
mycursor.execute("select * from  diary_data")
result = mycursor.fetchall() #fetch data 

    
print("ฟังก์ชั่นบันทึกและอ่านไดอารี่")

def check_word(w):
    if w != "" :
        if w == "อ่านไดอารี่ทั้งหมด":           
            read_diary()

        elif w == "เขียนไดอารี่":
            print("ใส่หัวข้อที่จะเขียนไดอารี่  และ บทความ ")  

        elif w == "อ่านไดอารี่ประจำวัน":
                select_diary()

    else : print("ฉันไม่เข้าใจในสิ่งที่คุณพูด หรือ พูดใหม่อีกครั้ง ")


def read_diary():#อ่านไดอารี่ทั้งหมด 
    for i in result:
        print(i)

def  select_diary():   
    mycursor.execute("select * from  diary_data WHERE date_diary='2019-12-06'")
    select = mycursor.fetchall() #fetch data 
    for s in select:
        print(s)

def insert_daiary(): 

    mycursor = mydb.cursor()
    sql = "INSERT INTO diary_data (toppic, detail_diary,date_diary) VALUES (%s,%s,%s)"
    value = ("ไปต่างจังหวัดกับครอบครัว","วันนี้เราได้ไปเที่ยวต่างจังหวัดกับครอบครัว ฉันมีความสุขมาก ","2019-12-10") 
    mycursor.execute(sql,value)
    mydb.commit()
    
#call function 
check_word("อ่านไดอารี่ทั้งหมด")
