from tkinter import *
import hashlib

s256 = hashlib.sha256()

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

def setBtnText(num):
    global count
    if num == 0 and btn0.cget("text") == "":
        if count % 2 == 0:
            btn0.config(text="O")
            count += 1
        else:
            btn0.config(text="X")
            count += 1       
    elif num == 1 and btn1.cget("text") == "":
        if count % 2 == 0:
            btn1.config(text="O")
            count += 1
        else:
            btn1.config(text="X")
            count += 1       
    elif num == 2 and btn2.cget("text") == "":
        if count % 2 == 0:
            btn2.config(text="O")
            count += 1
        else:
            btn2.config(text="X")
            count += 1       
    elif num == 3 and btn3.cget("text") == "":
        if count % 2 == 0:
            btn3.config(text="O")
            count += 1
        else:
            btn3.config(text="X")
            count += 1       
    elif num == 4 and btn4.cget("text") == "":
        if count % 2 == 0:
            btn4.config(text="O")
            count += 1
        else:
            btn4.config(text="X")
            count += 1       
    elif num == 5 and btn5.cget("text") == "":
        if count % 2 == 0:
            btn5.config(text="O")
            count += 1
        else:
            btn5.config(text="X")
            count += 1       
    elif num == 6 and btn6.cget("text") == "":
        if count % 2 == 0:
            btn6.config(text="O")
            count += 1
        else:
            btn6.config(text="X")
            count += 1       
    elif num == 7 and btn7.cget("text") == "":
        if count % 2 == 0:
            btn7.config(text="O")
            count += 1
        else:
            btn7.config(text="X")
            count += 1       
    elif num == 8 and btn8.cget("text") == "":
        if count % 2 == 0:
            btn8.config(text="O")
            count += 1
        else:
            btn8.config(text="X")
            count += 1

    if btn0.cget("text") == btn1.cget("text") and btn0.cget("text") == btn2.cget("text") and btn0.cget("text") == "O":
            print("O win") 
    if btn0.cget("text") == btn1.cget("text") and btn0.cget("text") == btn2.cget("text") and btn0.cget("text") == "X":
            print("X win") 

    if btn0.cget("text") == btn3.cget("text") and btn0.cget("text") == btn6.cget("text") and btn0.cget("text") == "O":
            print("O win") 
    if btn0.cget("text") == btn3.cget("text") and btn0.cget("text") == btn6.cget("text") and btn0.cget("text") == "X":
            print("X win")

    if btn0.cget("text") == btn4.cget("text") and btn0.cget("text") == btn8.cget("text") and btn0.cget("text") == "O":
            print("O win") 
    if btn0.cget("text") == btn4.cget("text") and btn0.cget("text") == btn8.cget("text") and btn0.cget("text") == "X":
            print("X win")

    if btn1.cget("text") == btn4.cget("text") and btn1.cget("text") == btn7.cget("text") and btn1.cget("text") == "O":
            print("O win")
    if btn1.cget("text") == btn4.cget("text") and btn1.cget("text") == btn7.cget("text") and btn1.cget("text") == "X":
            print("X win")

    if btn2.cget("text") == btn5.cget("text") and btn2.cget("text") == btn8.cget("text") and btn2.cget("text") == "O":
            print("O win")
    if btn2.cget("text") == btn5.cget("text") and btn2.cget("text") == btn8.cget("text") and btn2.cget("text") == "X":
            print("X win")

    if btn3.cget("text") == btn4.cget("text") and btn3.cget("text") == btn5.cget("text") and btn3.cget("text") == "O":
            print("O win")
    if btn3.cget("text") == btn4.cget("text") and btn3.cget("text") == btn5.cget("text") and btn3.cget("text") == "X":
            print("X win")

    if btn6.cget("text") == btn7.cget("text") and btn6.cget("text") == btn8.cget("text") and btn6.cget("text") == "O":
            print("O win")
    if btn6.cget("text") == btn7.cget("text") and btn6.cget("text") == btn8.cget("text") and btn6.cget("text") == "X":
            print("X win")
            
    if btn2.cget("text") == btn4.cget("text") and btn2.cget("text") == btn6.cget("text") and btn2.cget("text") == "O":
            print("O win")
    if btn2.cget("text") == btn4.cget("text") and btn2.cget("text") == btn6.cget("text") and btn2.cget("text") == "X":
            print("X win")

count = int(0)

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

btn0 = Button(window, text="", command=lambda:setBtnText(0)) 
btn0.grid(row=0, column=0, sticky=NSEW) 
btn1 = Button(window, text="", command=lambda:setBtnText(1))
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 = Button(window, text="", command=lambda:setBtnText(2))
btn2.grid(row=0, column=2, sticky=NSEW)

btn3 = Button(window, text="", command=lambda:setBtnText(3))
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 = Button(window, text="", command=lambda:setBtnText(4))
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 = Button(window, text="", command=lambda:setBtnText(5))
btn5.grid(row=1, column=2, sticky=NSEW)

btn6 = Button(window, text="", command=lambda:setBtnText(6))
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 = Button(window, text="", command=lambda:setBtnText(7))
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 = Button(window, text="", command=lambda:setBtnText(8))
btn8.grid(row=2, column=2, sticky=NSEW)


window.withdraw() #隱藏視窗
window.mainloop()