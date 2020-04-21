from tkinter import *
from tkinter import messagebox
import tkinter.messagebox

# ****** GLOBAL VARIABLES ******

objects = []
root = Tk()
root.withdraw()
root.title('Farhan Storage')

# ******* Start *******

class firstuse(object):

    loop = False
    attempts = 0

    def __init__(self, first):
        ftop = self.ftop = Toplevel(first)
        ftop.title('Input New Password')
        ftop.geometry('{}x{}'.format(300,175))
        ftop.resizable(width = False, height = False)
        self.lname = Label(ftop, text = " Username : ", font =('Arial', 14), justify = CENTER)
        self.lname.pack()
        self.fname = Entry(ftop, width = 30)
        self.fname.pack(pady = 7)
        self.lpass = Label(ftop, text = " Password : ", font =('Arial', 14), justify = CENTER)
        self.lpass.pack()
        self.fpass = Entry(ftop, show = "*", width = 30)
        self.fpass.pack(pady = 7)
        self.fbutton = Button(ftop, text = "Submit", command = self.firstsave, font = ('Arial', 14))
        self.fbutton.pack()

    def firstsave(self):
        self.value1 = self.fname.get()
        self.value2 = self.fpass.get()
        print(self.value1)
        print(self.value2)

'''class PopupWindow(object):

    def __init__(self, name, email, user):'''
        
        
w = firstuse(root)


root.mainloop()
