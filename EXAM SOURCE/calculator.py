from tkinter import*
from math import*
myWindow = Tk()


e = Entry(myWindow, width=60)
e.grid(row=0, column=0, columnspan=4)

def buttonClk(numb):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current+str(numb))
    return None

def btnCmd(opera):
    global num1, matOp
    matOp = opera
    num1 = int(e.get())
    e.delete(0, END)
    return None

def result():
    res = 0
    num2 = int(e.get())
    if matOp == "+":
        res = num1 + num2
    elif matOp == "-":
        res = num1 - num2
    elif matOp == "*":
        res = num1 * num2
    elif matOp == "**":
        res = num1 ** num2
    elif matOp == "//":
        res = num1 // num2
    
    e.delete(0, END)
    e.insert(0, str(res))
    return None

def specFucnt(command):
    num1 = int(e.get())
    res = 0
    if command == "Sqrt":
        res = sqrt(num1)
    elif command == "Fact":
        res = factorial(num1)
    e.delete(0, END)
    e.insert(0, str(res))
    return None


def clear():
    e.delete(0, END)
    num1 = ""
    matOp = ""
    return None


btn0 = Button(myWindow, text="0", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(0))
btn1 = Button(myWindow, text="1", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(1))
btn2 = Button(myWindow, text="2", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(2))
btn3 = Button(myWindow, text="3", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(3))
btn4 = Button(myWindow, text="4", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(4))
btn5 = Button(myWindow, text="5", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(5))
btn6 = Button(myWindow, text="6", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(6))
btn7 = Button(myWindow, text="7", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(7))
btn8 = Button(myWindow, text="8", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(8))
btn9 = Button(myWindow, text="9", padx=40, pady=20, font=("Helvetica", 24), command=lambda:buttonClk(9))

btnC = Button(myWindow, text="C", padx=40, pady=20, font=("Helvetica", 24), command=clear)
btnReiz = Button(myWindow, text="*", padx=48, pady=20, font=("Helvetica", 24), command=lambda:btnCmd("*"))
btnRes = Button(myWindow, text="=", padx=45, pady=71, font=("Helvetica", 24), command=result)
btnMin = Button(myWindow, text="-", padx=43, pady=20, font=("Helvetica", 24), command=lambda:btnCmd("-"))
btnPlus = Button(myWindow, text="+", padx=40, pady=20, font=("Helvetica", 24), command=lambda:btnCmd("+"))

btnSq = Button(myWindow, text="Sqrt", padx=20, pady=20, font=("Helvetica", 24), command=lambda:specFucnt("Sqrt"))
btnPow = Button(myWindow, text="x^y", padx=28, pady=20, font=("Helvetica", 24), command=lambda:btnCmd("**"))
btnFact = Button(myWindow, text="!", padx=43, pady=20, font=("Helvetica", 24), command=lambda:specFucnt("Fact"))
btnRem = Button(myWindow, text="//", padx=45, pady=20, font=("Helvetica", 24), command=lambda:btnCmd("//"))

btn7.grid(row=1, column=0,)
btn8.grid(row=1, column=1,)
btn9.grid(row=1, column=2,)
btnC.grid(row=1, column=3)

btn4.grid(row=2, column=0,)
btn5.grid(row=2, column=1,)
btn6.grid(row=2, column=2,)
btnReiz.grid(row=2, column=3)

btn3.grid(row=3, column=0,)
btn2.grid(row=3, column=1,)
btn1.grid(row=3, column=2,)
btnRes.grid(row=3, column=3, rowspan=2)

btn0.grid(row=4, column=0,)
btnPlus.grid(row=4, column=1,)
btnMin.grid(row=4, column=2,)

btnSq.grid(row=5, column=0,)
btnPow.grid(row=5, column=1,)
btnFact.grid(row=5, column=2,)
btnRem.grid(row=5, column=3,)

myWindow.mainloop()