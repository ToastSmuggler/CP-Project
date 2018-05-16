import tkinter as tk
window = tk.Tk()
wind2 = tk.Tk()
wind2.withdraw()
wind3 = tk.Tk()
wind3.withdraw()
wind4 = tk.Tk()
wind4.withdraw()
wind5 = tk.Tk()
wind5.withdraw()
window.title("Widgets Example")
use=""
pas=""
global alltogether
alltogether=[]
total=0

def callback():
    use=username.get()
    pas=password.get()
    print(use)
    print(pas)
    login(use,pas)
    username.delete(99999)
    password.delete(99999)

def callback2():
    global outof2
    global amountpeople2
    outof2=outoflbl.get()
    amountpeople2=amountpeoplelbl.get()
    print(outof2)
    print(amountpeople2)
    marks2(int(amountpeople2),int(outof2))
    outoflbl.delete(99999)
    amountpeoplelbl.delete(99999)

def callback3():
    dhfg=smlbl.get()
    gdrg=snlbl.get()
    print(dhfg)
    print(gdrg)
    marks3(dhfg,gdrg,outof2)    
    

def login(lusername,lpassword):
    b=False
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
                ##print(b)
                break
            else:
                continue
        else:
            continue
    if b==True:
        start()
    else:
        wrongpass()

def wrongpass():
    username.delete(99999)
    password.delete(99999)
    wrongpasslbl=tk.Label(window,text="Wrong username or password",bg="#FF0000")
    wrongpasslbl.pack()

def start():
    window.destroy()
    wind2.deiconify()
    wdywtdlbl=tk.Label(wind2,text="What do you\nwant to do?")
    wdywtdlbl.config(font=("Courier",50))
    marksbtn = tk.Button(wind2, text="Marks", command = marks)
    wdywtdlbl.pack(pady=15)
    marksbtn.pack()
    wind2.mainloop()

def marks():
    wind2.destroy()
    wind3.deiconify()
    global outoflbl
    global amountpeoplelbl
    dfgffdg=tk.Label(wind3,text="Marks system")
    dfgffdg.config(font=("Courier",25))
    dfgffdg.pack(pady=15)
    totals=0
    tk.Label(wind3,text="Out of:").pack()
    outoflbl=tk.Entry(wind3)
    outoflbl.pack()
    tk.Label(wind3,text="How many people?:").pack()
    amountpeoplelbl=tk.Entry(wind3,)
    submitbtn=tk.Button(wind3,command=callback2)
    amountpeoplelbl.pack()
    submitbtn.pack()
    wind3.mainloop()

def marks2(amountpeople,outof):
    global x
    wind3.destroy()
    x=False
    for i in range(amountpeople):
        x=False
        while x != True:
            global smlbl
            global snlbl
            wind4.deiconify()
            #sn=input("Student name: ")
            tk.Label(wind4,text="Student name:").pack()
            snlbl=tk.Entry(wind4)
            snlbl.pack()
            #sm=int(input("Student mark (out of {})".format(outof)))
            tk.Label(wind4,text="Student mark:").pack()
            smlbl=tk.Entry(wind4)
            smlbl.pack()
            submitbtn2=tk.Button(wind4,command=callback3)
            submitbtn2.pack()            
        
#    for i in range(len(tname)):
#        jsds.append("{}:{}:{}".format(tmark[i],tname[i],tperc[i]))
    alltogether.sort()
    totala=total%amountpeople
    print("Average mark: {}".format(totala))
    for i in range(amountpeople):
        print(alltogether[i])
        
    hiks=yorn("Would you like to save these marks? ")
    if hiks == True:
        filename=input("Enter a file name: ")
        f=open("{}.txt".format(filename),"a+")
        for i in range(len(alltogether)):
            f.write("\n{}".format(alltogether[i]))
        f.close()
        print("Done!")
        print("Saved at \"/{}\"".format(filename))
    else:
        print("Ok.")
        init()
    
def marks3(mark,name,outof):
    global total
    if mark <= outof:
        perc=str((round(mark/outof,1)%100))
        alltogether.append("{}:{}:{}".format(mark,name,perc))
        x=True
        total += mark
    else:
        wlbl=tk.Label(wind4,text="Incorrect mark input",bg="#FF0000")
        wlbl.pack() 
        x=False       
        return 

def init():
    start()    
loginlbl=tk.Label(window, text="Login")
ulbl = tk.Label(window, text="Username:")
username = tk.Entry(window, text="username")
plbl = tk.Label(window, text="Password:")
password = tk.Entry(window, text="password", show="*")
btn = tk.Button(window, text="Login", command=callback)




loginlbl.config(font=("Courier",50))
loginlbl.pack(pady=15)
ulbl.pack()
username.pack()
plbl.pack()
password.pack()
btn.pack()

window.mainloop()