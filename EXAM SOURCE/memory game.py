from multiprocessing.connection import answer_challenge
from tkinter import*
from tkinter import messagebox
import random


myObj = Tk()
myObj.title("Memory game")
count = 0
correctAnsw = 0
answ = list()
answ_dict = dict()
numList = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(numList)



def newGame():
    global correctAnsw, count, answ_dict, answ
    count = 0
    answ = []
    answ_dict = {}
    random.shuffle(numList)

    for key in [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11]:
      key['state'] = NORMAL
      key['bg'] = '#12CA00'
      key['text'] = ""
    
    return None

def about():
    newWin = Toplevel()
    newWin.title("Par autoru")
    newWin.geometry("200x200")
    lblAbout = Label(newWin, text = "Dairis Mivreniks 11B")
    lblAbout.grid(row=0, column=0)
    return None

sljapa = Menu(myObj)
myObj.config(menu = sljapa)
sljapa.add_command(label = "Jauna spēle", command=newGame)
sljapa.add_command(label = "Par autoru", command=about)
sljapa.add_command(label = "Iziet", command=myObj.quit)

def btnClick(btn, number):
    global correctAnsw, count, answ_dict, answ
    if btn['bg'] == '#12CA00' and count < 2:
        btn['bg'] = '#A0FF96'
        btn['text'] = numList[number]
        answ.append(number)
        answ_dict[btn] = numList[number]
        count += 1

    if len(answ) == 2:
        if numList[answ[0]] == numList[answ[1]]:
            for key in answ_dict:
                key['state'] = DISABLED
            correctAnsw += 1
            if correctAnsw == 6:
                messagebox.showinfo("Memory Game", "YOU WON!")

        else:
            messagebox.showinfo("Memory Game", "Nope")
            for key in answ_dict:
                key['bg'] = '#12CA00'
                key['text'] = ""
        
        count = 0
        answ = []
        answ_dict = {}
    return None

btn0 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn0, 0))
btn1 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn1, 1))
btn2 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn2, 2))
btn3 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn3, 3))
btn4 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn4, 4))
btn5 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn5, 5))
btn6 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn6, 6))
btn7 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn7, 7))
btn8 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn8, 8))
btn9 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn9, 9))
btn10 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn10, 10))
btn11 = Button(myObj, bg = "#12CA00", width=10, height=5, font=("Helvetiva", 13), command = lambda:btnClick(btn11, 11))  

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)

btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=1, column=2)

btn6.grid(row=2, column=0)
btn7.grid(row=2, column=1)
btn8.grid(row=2, column=2)

btn9.grid(row=3, column=0)
btn10.grid(row=3, column=1)
btn11.grid(row=3, column=2)



myObj.mainloop()