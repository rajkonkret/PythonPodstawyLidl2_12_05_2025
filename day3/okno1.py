import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text="Witaj Świeci")

        self.label.pack(side="top")
        tkinter.mainloop()


my_gui = MyGui()
