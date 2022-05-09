from cgi import test
from ipaddress import collapse_addresses
from mailbox import linesep
from tkinter import*
from tkinter import messagebox
from tkinter import font
from tkinter.ttk import Labelframe
import webbrowser
from datetime import date, timedelta


def generateDate(start_date, end_date):
    for i in range (int((end_date - start_date).days)):
        yield start_date + timedelta(i)



def openFile(file_name):
    try:
        with open(file_name) as f:
            lines = f.readlines()
            if len(lines) == 0:
                return None
            f.close()
            return lines
    except:
        return None


def addRecord():
    data_row = input_window.get()
    real_data = work_list.get(0, END)
    if real_data[0] == "No Data!":
        work_list.config(state=NORMAL)
        work_list.delete(0, END)

    work_list.insert(END, data_row)
    input_window.delete(0, END)
    return None


def sortRecords():
    real_data = list(work_list.get(0, END))
    real_data.sort()
    work_list.delete(0, END)
    for lines in real_data:
        work_list.insert(END, lines)
    
    return None


def delRecords():
    dataDelete = work_list.curselection()
    if len(dataDelete) == 0:
        messagebox.showerror("Error", "Not Selected!")
    else:
        work_list.delete(dataDelete[0])

    return None 


def saveRecord():
    file_name = "planner_data.txt"
    try:
        raw_data = work_list.get(0, END)
        with open(file_name, "w") as f:
            for lines in raw_data:
                f.write(lines)
        f.close()
        messagebox.showinfo("Info", "All Saved!")
    
    except:
        messagebox.showerror("Error", "Not Saved*")

    return None


myObj = Tk()
myObj.title("Darbu plānotājs")
myObj.geometry("800x600")

dateFrame = LabelFrame(myObj, text="Darbu Kalendārs", font=("Helvetica", 21))
dateFrame.grid(row=0, column=2)

start_date = date(2022,4,1)
end_date = date(2022,4,30)
btnList = []

counter = 1

for datums in generateDate(start_date, end_date):
    btnName = "btn" + str(counter)
    collumnCounter = 2
    rowCounter = 1
    newButton = Button(dateFrame, text=btnName, width=6, height=3, padx=10, pady=5)
    btnList.append(newButton)
    counter += 1


for btn in btnList:
    btn.grid(row = rowCounter, column = collumnCounter)
    collumnCounter += 1
    counter += 1
    if collumnCounter == 8:
        collumnCounter = 2
        rowCounter += 1


work_frame = LabelFrame(myObj, text="Šodienas darbi", font=("Helvetica", 21))
work_list = Listbox(work_frame, width=20, height=13, font=("Helvetica", 15))
input_window = Entry(myObj, width=20, font=("Helvetica", 15), background="grey")


file_name = "planner_data.txt"
data = openFile(file_name)
if data != None:
    for lines in data:
        work_list.insert(END, lines)

else: 
    work_list.insert(END, "No Data!")
    work_list.config(state=DISABLED)


btnAdd = Button(myObj, text="Pievienot", font=("Helvetica", 15), padx=20, pady=10, command=addRecord)
btnSort = Button(myObj, text="Kārtot", font=("Helvetica", 15), padx=20, pady=10, command=sortRecords)
btnDel = Button(myObj, text="Delete", font=("Helvetica", 15), padx=20, pady=10, command=delRecords)
btnSave = Button(myObj, text="Save", font=("Helvetica", 15), padx=20, pady=10, command=saveRecord)



work_frame.grid(row=0, column=0, columnspan=2)
work_list.grid(row=1, column=0, columnspan=2)
input_window.grid(row=2, column=0, columnspan=2)

btnAdd.grid(row=3, column=0)
btnSort.grid(row=3, column=1)
btnDel.grid(row=4, column=0)
btnSave.grid(row=4, column=1)


myObj.mainloop()