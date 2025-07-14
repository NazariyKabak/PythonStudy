import tkinter
class MyGUI:
    def __init__(self):
        # створити віджет головного вікнп
        self.main_window = tkinter.Tk()
        # Рамка
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # Title
        self.main_window.title("My First GUI!")
        # віджет лейбл, який має напис
        self.label1 = tkinter.Label(self.top_frame, text="Мигнуть!")
        self.label2 = tkinter.Label(self.top_frame, text="Моргнуть!")
        self.label3 = tkinter.Label(self.top_frame, text="Кивнуть!")

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')


        self.label4 = tkinter.Label(self.bottom_frame, text="Bebra!")
        self.label5 = tkinter.Label(self.bottom_frame, text="Neyzr!")
        self.label6 = tkinter.Label(self.bottom_frame, text="Chips!")

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # викликати віджет
        self.top_frame.pack()
        self.bottom_frame.pack()
        # увійти в цикл ткінтера
        tkinter.mainloop()