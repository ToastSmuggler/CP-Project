import tkinter as tk
window = tk.Tk()
wind2 = tk.Tk()
wind2.withdraw()
wind3 = tk.Tk()
wind3.withdraw()
window.title("Widgets Example")
use=""
pas=""

def callback():
    use=username.get()
    pas=password.get()
    print(use)
    print(pas)
    login(use,pas)
    username.delete(99999)
    password.delete(99999)

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
    submitbtn=tk.Button(wind3)
    amountpeoplelbl.pack()
    wind3.mainloop()
    outof=outoflbl.get()
    amountpeople=amountpeoplelbl.get()
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
    for i in range(len(tmark)):
        totals+=tmark[i]
    total=totals%len(tmark)
    print("Average mark: {}".format(total))
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