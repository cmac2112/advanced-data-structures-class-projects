#tkinter ex 2

import tkinter
class MYGUI:
    def __init__(self):
        #create main window widget
        self.main_window = tkinter.Tk()

        #display title
        self.label = tkinter.Label(self.main_window, text='Hello')

        self.label.pack()

        tkinter.mainloop() #not working

if __name__ == '__main__':
    my_gui = MYGUI()
