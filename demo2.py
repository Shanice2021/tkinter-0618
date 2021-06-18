from tkinter import *
import hashlib

s256 = hashlib.sha256()
s1 = hashlib.sha1()
m5 = hashlib.md5()

def login():
    idData = entryID.get() 
    pwData = entryPW.get()
    if len(idData) > 0 and len(pwData) > 0: 
        s256.update(idData.encode("utf-8"))
        idHash = s256.hexdigest()
        # print(idHash)csie
        s256.update(pwData.encode("utf-8"))
        pwHash = s256.hexdigest()
        # print(pwHash)h3041723
        if idHash == "207a0fd942624d8c7d26cb85594480f37840acfbf399f6cdc3724774ba9f1931" and pwHash == "f9f5f0356349d2339b1ee1e3a3e53be445c338c6a09814cdbc53979d96899420":
            window.deiconify() # 取消隱藏視窗
            top.destroy() 
        else:
            entryID.delete(0, "end") 
            entryPW.delete(0, "end")
    else:
        entryID.delete(0, "end") 
        entryPW.delete(0, "end")       

def exitProgram():
    top.destroy()
    window.destroy()

def search():
    hashIDData = entryhashID.get()
    s256.update(hashIDData.encode("utf-8"))
    idHashs256 = s256.hexdigest()
    print("idHashs256:"+idHashs256)
    idHashs1 = s1.hexdigest()
    print("idHashs1:"+idHashs1)
    idHashm5 = m5.hexdigest()
    print("idHashm5:"+idHashm5)







window = Tk()
window.geometry("400x300+200+100")

top = Toplevel(window) # 子視窗 關閉後不會停止該程式
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


window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)


hashID = Label(window, text="hash code", anchor=E, justify=RIGHT, font=("Times", 20))
entryhashID = Entry(window)
btnSearch = Button(window, text="Search", command=search)
hashAns = Label(window, text="原密碼:", anchor=W, justify=LEFT, font=("Times", 20))
hashCode = Label(window, text="雜湊函式:", anchor=W, justify=LEFT, font=("Times", 20))

hashID.grid(row=0, column=0, sticky=NSEW)
entryhashID.grid(row=0, column=1, sticky=NSEW)
btnSearch.grid(row=0, column=2, sticky=NSEW)
hashAns.grid(row=1, columnspan=3, sticky=NSEW)
hashCode.grid(row=2, columnspan=3, sticky=NSEW)















window.withdraw() #隱藏視窗
window.mainloop()