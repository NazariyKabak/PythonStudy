import tkinter
import tkinter.messagebox
class GuiEntry:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text="Введіть відстань в км: ")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Порахувати', command=self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame, text='Quite', command=self.main_window.destroy)

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6
        tkinter.messagebox.showinfo('Результат', str(kilo) + ' Kilo' + str(miles) + ' Miles')
