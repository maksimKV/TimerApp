from tkinter import *
#import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

#window = Tk()
#window.geometry("600x600")
#window.title("Timer app")
#window.mainloop()

class TimerApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (AddInterval, EditInterval):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AddInterval")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class AddInterval(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.breakSeconds = []
        self.breakMinutes = []
        self.intervalSeconds = []
        self.intervalMinutes =[]

        beginingLabel: Label = Label(self, text="Please enter as many sequences and intervals you like")
        beginingLabel.pack()

        intervalLabel: Label = Label(self, text="Enter interval time", bg="white")
        intervalLabel.pack()

        intervalSecondsLabel: Label = Label(self, text="Enter interval seconds", bg="white")
        intervalSecondsLabel.pack()

        intervalSecondsSpinbox: Spinbox = Spinbox(self, to=59, state="readonly")
        self.intervalSeconds.append(intervalSecondsSpinbox)
        intervalSecondsSpinbox.pack()

        intervalMinutesLabel: Label = Label(self, text="Enter interval minutes", bg="white")
        intervalMinutesLabel.pack()

        intervalMinutesSpinbox: Spinbox = Spinbox(self, to=720, state="readonly")
        self.intervalMinutes.append(intervalMinutesSpinbox)
        intervalMinutesSpinbox.pack()

        addIntervalButton: Button = Button(self, text="Add New Interval", command=self.addInterval)
        addIntervalButton.pack()

        saveIntervalButton: Button = Button(self, text="Save New Interval", command=self.saveInterval)
        saveIntervalButton.pack()

    def addInterval(self):
        breakLabel: Label = Label(self, text="Enter break time", bg="white")
        breakLabel.pack()

        breakSecondsLabel: Label = Label(self, text="Enter break seconds", bg="white")
        breakSecondsLabel.pack()

        breakSecondsSpinbox: Spinbox = Spinbox(self, to=59, state="readonly")
        self.breakSeconds.append(breakSecondsSpinbox)
        breakSecondsSpinbox.pack()

        breakMinutesLabel: Label = Label(self, text="Enter break minutes", bg="white")
        breakMinutesLabel.pack()

        breakMinutesSpinbox: Spinbox = Spinbox(self, to=720, state="readonly")
        self.breakMinutes.append(breakMinutesSpinbox)
        breakMinutesSpinbox.pack()


        intervalLabel: Label = Label(self, text="Enter interval time", bg="white")
        intervalLabel.pack()

        intervalSecondsLabel: Label = Label(self, text="Enter interval seconds", bg="white")
        intervalSecondsLabel.pack()

        intervalSecondsSpinbox: Spinbox = Spinbox(self, to=59, state="readonly")
        self.intervalSeconds.append(intervalSecondsSpinbox)
        intervalSecondsSpinbox.pack()

        intervalMinutesLabel: Label = Label(self, text="Enter interval minutes", bg="white")
        intervalMinutesLabel.pack()

        intervalMinutesSpinbox: Spinbox = Spinbox(self, to=720, state="readonly")
        self.intervalMinutes.append(intervalMinutesSpinbox)
        intervalMinutesSpinbox.pack()

    def saveInterval(self):
        messagebox.showinfo("Interval Seconds", self.getIntervalSeconds(self))
        #messagebox.showinfo("Title", getIntervals())
        #w = Label(separator, text=intervals, bg="white")
        #w.pack()

    def getIntervalSeconds(self):
        values = [intervalSecondsSpinbox.get() for intervalSecondsSpinbox in self.intervalSeconds]
        return values

class EditInterval(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()