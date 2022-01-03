"""
Created on Sunday 2022 01 02

@author: Reza Ferdowsi
"""
############################# Tutorial1- Creating Simple Programs #######################
from datetime import datetime
def yourage():
    name = input("please type your name: ")
    DOB = input("please type your date of birth: (2002 Jan 02) ")
    DOB_edited = datetime.strptime(DOB, '%Y %b %d')
    age = (datetime.now()).year - DOB_edited.year
    print(f"Hi {name} your age is {age}.")
    return age
# yourage()

############################# 
def username_password():
    name = input("type your name: ")
    last_name = input("type your last name: ")
    username= name[0]+"."+last_name
    f_n = int(input("type your favorite number: (between 1 and 5) "))
    f= input("give me a short text:  ").lower()
    if len(f)>5:
        i= f.find(" ")
        f= f[:i]+str(f_n)+f[i:]
        p=f.replace(" ","")
        password=""
        for i in range(len(p)):
            if i % f_n == 0:
                password+=p[i].upper()
            else:
                password+=p[i]
        print(f"your username and password are: {username} / {password}")
    else:
        print("your text is too short :( ") 
username_password()                   
                