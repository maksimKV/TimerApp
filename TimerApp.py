from tkinter import *
from tkinter import messagebox
import TimerClass

window = Tk()
window.geometry("600x600")
window.title("Timer App")

breakSeconds = []
breakMinutes = []
intervalSeconds = []
intervalMinutes =[]

def addInterval(separator):
    breakLabel: Label = Label(separator, text="Enter break time", bg="white")
    breakLabel.pack()

    breakSecondsLabel: Label = Label(separator, text="Enter break seconds", bg="white")
    breakSecondsLabel.pack()

    breakSecondsSpinbox: Spinbox = Spinbox(separator, to=59, state="readonly")
    breakSeconds.append(breakSecondsSpinbox)
    breakSecondsSpinbox.pack()

    breakMinutesLabel: Label = Label(separator, text="Enter break minutes", bg="white")
    breakMinutesLabel.pack()

    breakMinutesSpinbox: Spinbox = Spinbox(separator, to=720, state="readonly")
    breakMinutes.append(breakMinutesSpinbox)
    breakMinutesSpinbox.pack()


    intervalLabel: Label = Label(separator, text="Enter interval time", bg="white")
    intervalLabel.pack()

    intervalSecondsLabel: Label = Label(separator, text="Enter interval seconds", bg="white")
    intervalSecondsLabel.pack()

    intervalSecondsSpinbox: Spinbox = Spinbox(separator, to=59, state="readonly")
    intervalSeconds.append(intervalSecondsSpinbox)
    intervalSecondsSpinbox.pack()

    intervalMinutesLabel: Label = Label(separator, text="Enter interval minutes", bg="white")
    intervalMinutesLabel.pack()

    intervalMinutesSpinbox: Spinbox = Spinbox(separator, to=720, state="readonly")
    intervalMinutes.append(intervalMinutesSpinbox)
    intervalMinutesSpinbox.pack()

def saveInterval():
    messagebox.showinfo("Interval Seconds", getIntervalSeconds())
    #messagebox.showinfo("Title", getIntervals())
    #w = Label(separator, text=intervals, bg="white")
    #w.pack()

def getIntervalSeconds():
    values = [intervalSecondsSpinbox.get() for intervalSecondsSpinbox in intervalSeconds]
    return values

beginingLabel: Label = Label(window, text="Please enter as many sequences and intervals you like")
beginingLabel.pack()

separator: Frame = Frame(bd=1, padx=5, pady=10, relief=SUNKEN, bg="white")
separator.pack(fill=X, padx=5, pady=5)

intervalLabel: Label = Label(separator, text="Enter interval time", bg="white")
intervalLabel.pack()

intervalSecondsLabel: Label = Label(separator, text="Enter interval seconds", bg="white")
intervalSecondsLabel.pack()

intervalSecondsSpinbox: Spinbox = Spinbox(separator, to=59, state="readonly")
intervalSeconds.append(intervalSecondsSpinbox)
intervalSecondsSpinbox.pack()

intervalMinutesLabel: Label = Label(separator, text="Enter interval minutes", bg="white")
intervalMinutesLabel.pack()

intervalMinutesSpinbox: Spinbox = Spinbox(separator, to=720, state="readonly")
intervalMinutes.append(intervalMinutesSpinbox)
intervalMinutesSpinbox.pack()

addIntervalButton: Button = Button(separator, text="Add New Interval", command=lambda: addInterval(separator))
addIntervalButton.pack()

saveIntervalButton: Button = Button(separator, text="Save New Interval", command=saveInterval)
saveIntervalButton.pack()

window.mainloop()