from tkinter import *
import hashlib

s256 = hashlib.sha256()
btnLabs = ["7", "8", "9", "/",
           "4", "5", "6", "*",
           "1", "2", "3", "-",
           "0", ".", "(", "+",
           ")", "C", "exit", "="]   


def login():
    idData = entryID.get()
    pwData = entryPW.get()
    if len(idData) > 0 and len(pwData) > 0:
        s256.update(idData.encode("utf-8"))
        idHash = s256.hexdigest()
        s256.update(pwData.encode("utf-8"))
        pwHash = s256.hexdigest()
        print(idHash)#h103
        print(pwHash)#1234
        if idHash == "569a5984cff7a922ff65241d72cdbeac2c9558eb685352f9e431a533be0b6eb1" and pwHash == "7499ef90eea01df5385077ee951693d56d1fe7bb02858b2e868a613ca5c139c1":
            root.deiconify() 
            top.destroy() 
        else:
            entryID.delete(0, "end") 
            entryPW.delete(0, "end")
    else:
        entryID.delete(0, "end") 
        entryPW.delete(0, "end")       

def exitProgram():
    top.destroy()
    root.destroy()

def click(btnStr):
    return lambda:btnClick(btnStr)

def btnClick(btnStr):
    if btnStr == "exit":
        root.destroy()
    elif btnStr in ["+", "-", "*", "/", "(", ")", "."] or btnStr in map(str, range(0, 10)):
        if calLab["text"] == "0":
            calLab["text"] = btnStr
        else:
            calLab["text"] += btnStr
    elif btnStr == "=":
        calLab["text"] = str(eval(calLab["text"])) 
    elif btnStr == "C":
        calLab["text"] = "0" #清空

root = Tk()
root.geometry("400x300+200+100")
top = Toplevel(root)
labID = Label(top, text="ID", anchor=E, justify=RIGHT, font=("Times", 20))
labPW = Label(top, text="Password", anchor=E, justify=RIGHT, font=("Times", 20))
entryID = Entry(top)
entryPW = Entry(top, show="*")
btnLogin = Button(top, text="Login", command=login)
btnExit = Button(top, text="Exit", command=exitProgram)
labID.grid(row=0, column=0, sticky=NSEW)
entryID.grid(row=0, column=1, sticky=NSEW)
labPW.grid(row=1, column=0, sticky=NSEW)
entryPW.grid(row=1, column=1, sticky=NSEW)
btnLogin.grid(row=2, column=0, sticky=NSEW)
btnExit.grid(row=2, column=1, sticky=NSEW)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

calLab = Label(root, text="0", bg="#ccffdd", font=("Times", 20), anchor=E, justify=RIGHT)
calLab.grid(row=0, column=0, sticky=NSEW, columnspan=4)

i = 0
btns = []
for btnLab in btnLabs:
    btn = Button(root, text=btnLab, command=click(btnLab), font=("Times", 20))
    btns.append(btn)
    btn.grid(row = i // 4 + 1, column = i % 4, sticky=NSEW)
    i += 1


root.withdraw()
root.mainloop()