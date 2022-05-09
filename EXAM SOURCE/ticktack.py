from tkinter import*
from tkinter import messagebox

myObj = Tk()
myObj.title("Tic Tac Toe!")
global playerX, count, winner
playerX = True
count = 0
winner = False

def newGame():
    global playerX, count, winner
    winner = False
    count = 0
    playerX = True
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1["text"] = ""
    btn2["text"] = ""
    btn3["text"] = ""
    btn4["text"] = ""
    btn5["text"] = ""
    btn6["text"] = ""
    btn7["text"] = ""
    btn8["text"] = ""
    btn9["text"] = ""
    return None


sljapa = Menu(myObj)
myObj.config(menu = sljapa)
sljapa.add_command(label = "New Game", command=newGame)
sljapa.add_command(label = "Quit", command=myObj.quit)

btn1 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn1))
btn2 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn2))
btn3 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn3))
btn4 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn4))
btn5 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn5))
btn6 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn6))
btn7 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn7))
btn8 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn8))
btn9 = Button(myObj, text="", width=10, height=5, font=("Helvetica", 24), command=lambda:tick(btn9))


btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)



def tick(button):
    global playerX, count
    if button["text"] == "" and playerX == True:
        button["text"] = "X"
        playerX = False
        count +=1

    elif button["text"] == "" and playerX == False:
        button["text"] = "O"
        playerX = True
        count +=1
    
    else:
        messagebox.showerror("TickTak", "Aizņemts!")
    winCheck()    
    return None


def winCheck():
    global winner
    winner = False

    if (btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X"
    or btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X"
    or btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X"
    or btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X"
    or btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X"
    or btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X"
    or btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X"
    or btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X"):
        winner = True
        messagebox.showinfo("TickTak", "Uzvareja X!")
        disableBtn()

    elif (btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O"
    or btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O"
    or btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O"
    or btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O"
    or btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O"
    or btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O"
    or btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O"
    or btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O"):
        winner = True
        messagebox.showinfo("TickTak", "Uzvareja O!")
        disableBtn()

    elif winner == False and count == 9:
        messagebox.showinfo("TickTak", "Neizskirts")
        disableBtn()

def disableBtn():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return None


myObj.mainloop()