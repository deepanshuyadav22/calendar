#to implement GUI
from tkinter import *

#to display error message
from tkinter import messagebox

#to get calendar of chosen month or chosen year
import calendar

#to get calendar of current month or current year
from datetime import date

#Designing Main Window----------------------------------------------------

#creating main window
w = Tk()

#title of main window
w.title("Calendar")

#size of main window
w.geometry("882x590")

#background colour of main window
w.configure(background = '#fff')

#Functions----------------------------------------------------------------

def printCalendar(cal):
    text_displayCalendar.config(state = "normal")
    text_displayCalendar.delete("1.0", "end")
    text_displayCalendar.insert(END, cal)
    text_displayCalendar.config(state = "disabled")

def currentMonth(event):
    yyyy = date.today().year #getting current year
    mm = date.today().month #getting current month
    cal = calendar.month(yyyy, mm, 9)
    printCalendar(cal)

def currentYear(event):
    yyyy = date.today().year
    cal = calendar.calendar(yyyy)
    printCalendar(cal)

def goToDate(event):
    try:
        yyyy = int(entry_enterYear.get())
        mm = month_is.get()

        if mm == "-Select-":
            cal = calendar.calendar(yyyy)
        else:
            mm = months.index(mm)
            cal = calendar.month(yyyy, mm, 9)
        printCalendar(cal)
    except:
        #if 'entry_enterYear' is empty or not holding
        #a numeric value, then this part will be executed
        messagebox.showinfo("Error", "Enter valid year.")

#Heading------------------------------------------------------------------

heading = Label(w, text = "Calendar", bg = '#fff', font = ('algerian', 25))
heading.config(pady = 20)
heading.pack()

#Output Display Section---------------------------------------------------

text_displayCalendar = Text(w, width = '55', height = '19', bg = '#f1f1f1', wrap = WORD, bd = '0', font = ('calibri', 14))

text_displayCalendar.insert(END, calendar.month(date.today().year, date.today().month, 9))
text_displayCalendar.config(state = "disabled")
text_displayCalendar.pack()
text_displayCalendar.place(x = 50, y = 100)

#Buttons------------------------------------------------------------------

button_currentMonth = Button(w, text = "Current Month", width = 15, height = 2, bg = '#077bff', fg = '#fff', activebackground = 'blue', activeforeground = '#fff', font = ('centurygothic', 14), bd = 0)
button_currentYear = Button(w, text = "Current Year", width = 15, height = 2, bg = '#077bff', fg = '#fff', activebackground = 'blue', activeforeground = '#fff', font = ('centurygothic', 14), bd = 0)
button_go = Button(w, text = "Go", width = 15, height = 2, bg = '#077bff', fg = '#fff', activebackground = 'blue', activeforeground = '#fff', font = ('centurygothic', 14), bd = 0)

button_currentMonth.pack()
button_currentYear.pack()
button_go.pack()

button_currentMonth.bind('<Button-1>', currentMonth)
button_currentYear.bind('<Button-1>', currentYear)
button_go.bind('<Button-1>', goToDate)

button_currentMonth.place(x = 655, y = 100)
button_currentYear.place(x = 655, y = 180)
button_go.place(x = 655, y = 480)

#Month Selection Section-----------------------------------------

label_chooseMonth = Label(w, text = "Choose month:", bg = '#fff', font = ('segoeui', 14))
label_chooseMonth.pack()
label_chooseMonth.place(x = 652, y = 320)

months = ["-Select-", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_is = StringVar()

#setting default value of month
month_is.set("-Select-")

#creating month list UI
month_list = OptionMenu(w , month_is, *months)

month_list.config(bg = '#f2f2f2', bd = 0, font = ('calibri', 12))
month_list["menu"].config(bg = '#f5f5f5', bd = 0, font = ('calibri', 12))
month_list.pack()
month_list.place(x = 655, y = 350)

#Year Enter Section-------------------------------------------------------

label_enterYear = Label(w, text = "Enter year:", bg = '#fff', font = ('segoeui', 14))
entry_enterYear = Entry(width = '17', bg = '#f1f1f1', bd = '0', font = ('calibri', 14))

#default value of 'entry_enterYear' is current year
entry_enterYear.insert(END, date.today().year)

label_enterYear.pack()
entry_enterYear.pack()

label_enterYear.place(x = 652, y = 400)
entry_enterYear.place(x = 655, y = 430)


#Displaying 'OR'----------------------------------------------------------

label_displayOR = Label(w, text = "OR", bg = '#fff', font = ('segoeui', 16))
label_displayOR.pack()
label_displayOR.place(x = 715, y = 268)

#-------------------------------------------------------------------------

w.mainloop()
