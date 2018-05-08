import time
import random
#import sqlite3
#conn = sqlite3.connect('example.db')
#c = conn.cursor()
name=[]
mark=[]
perc=[]
tname=[]
tmark=[]
tperc=[]
jsds=[]

def yorn(ndfn):
    adgs=input(ndfn)
    if adgs.lower() == "y" or "yes" or "ye" or "yup" or "yeah" or "yea":
        return True
    else:
        return False

def isequal(A,B):
    if A == B:
        return True
    else:
        return False

def register():
    print("Welcome please create an account to:")                                                                                           
    passsame=False
    rusername=""
    password1=""
    password2=""
    while passsame != True:
        rusername=input("Choose a Username:")
        rusername=rusername.lower()
        password1=input("Choose a Password:")
        password2=input("Repeat the Password Again:")
        passsame=isequal(password1,password2)
    utp="{}:{}".format(rusername,password1)
    f=open("utp.txt","a+")
    f.write("\n{}".format(utp))
    f.close()
    print("Registered!")
    init()

def login():
    print("Welcome back please login:")   
    b=False
    lusername=input("Username:").lower()
    lpassword=input("Password:")
    f=open("utp.txt","r")
    for line in f:
        if line != "\n":
            a=line.split(":")
            #print(a)
            username=a[0]
            password=a[1]
            password=password.strip("\n")
            #print(sp)
            if lusername==username and lpassword==password:
                b=True
                break
            else:
                print("Incorrect username / password")
                continue
        else:
            continue
    if b==True:
        start()
    else:
        login()


def init():
    print("Would you like to (R)egister or (S)ign-in?")
    initin=input()
    if initin.lower()=="r":
        register()
    else:
        login()

def start():
    marks()

def marks():
    outof=int(input("Out of:"))
    amountpeople=int(input("How many people?:"))
    x=False
    for i in range(amountpeople):
        x=False
        while x != True:
            sn=input("Student name: ")
            sm=int(input("Student mark (out of {})".format(outof)))
            sp="{}%".format(round(100*(sm/outof))) 
            if sm <= outof and sm >= 0:
                x=True
            else:
                x=False
        tname.append(sn)
        tmark.append(sm)
        tperc.append(sp)
    for i in range(len(tname)):
        jsds.append("{}:{}:{}".format(tmark[i],tname[i],tperc[i]))
    jsds.sort()
    for i in range(len(tname)):
        print(jsds[i])
        
    hiks=yorn("Would you like to save these marks? ")
    if hiks == True:
        filename=input("Enter a file name: ")
        f=open("{}.txt".format(filename),"a+")
        for i in range(len(jsds)):
            f.write("\n{}".format(jsds[i]))
        f.close()
        print("Done!")
        print("Saved at \"/{}\"".format(filename))
    else:
        print("Ok.")
        init()




init()
#marks()
#conn.close()
