#tkinter 3

import tkinter

class MYGUI:
    def __init__(self):
        #create main window
        self.main_window = tkinter.Tk()

        #create two lavel widgets with solid boarders
        self.label1 = tkinter.Label(self.main_window,
                                    text='Hello',
                                    borderwidth=1,
                                    relief='solid')
        self.label2 = tkinter.Label(self.main_window,
                                    text='This is my gui program.',
                                    borderwidth=1,
                                    relief='solid')
        #display lavels with 20 pixels of horizontal and vertical padding
        self.label1.pack(padx=20, pady=20)
        self.label2.pack(padx=20, pady=20)

        #nter tkinter main loop
        tkinter.mainloop()
if __name__ == '__main__':
    my_gui = MYGUI()
