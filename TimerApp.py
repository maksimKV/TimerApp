from tkinter import *
from tkinter import messagebox
import TimerClass

window = Tk()
window.geometry("600x600")
window.title("Timer App")

intervals = []
breaks = []

def addInterval(separator):
    breakLabel: Label = Label(separator, text="Enter break time", bg="white")
    breakLabel.pack()

    breakEntry: Entry = Entry(separator)
    breaks.append(breakEntry)
    breakEntry.pack()

    intervalLabel: Label = Label(separator, text="Enter interval time", bg="white")
    intervalLabel.pack()

    entry: Entry = Entry(separator)
    intervals.append(entry)
    entry.pack()

def saveInterval():
    messagebox.showinfo("Title", getIntervals())
    w = Label(separator, text=intervals, bg="white")
    w.pack()

def getIntervals():
    return [int(entry.get()) for entry in intervals]

def getBreaks():
    return [int(entry.get() for entry in breaks)]

beginingLabel: Label = Label(window, text="Please enter as many sequences and intervals you like")
beginingLabel.pack()

separator: Frame = Frame(bd=1, padx=5, pady=10, relief=SUNKEN, bg="white")
separator.pack(fill=X, padx=5, pady=5)

intervalLabel: Label = Label(separator, text="Enter interval time", bg="white")
intervalLabel.pack()

entry: Entry = Entry(separator)
intervals.append(entry);
entry.pack()

addIntervalButton: Button = Button(separator, text="Add New Interval", command=lambda: addInterval(separator))
addIntervalButton.pack()

saveIntervalButton: Button = Button(separator, text="Save New Interval", command=saveInterval)
saveIntervalButton.pack()

window.mainloop()