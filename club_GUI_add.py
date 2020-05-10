import tkinter

from load_save import load_info
from load_save import save_info

FILENAME = 'ClubInfo.dat'


class AddClubInfoGUI:
    def __init__(self):
        # Create window
        self.window = tkinter.Tk(className="社團資訊系統")
        self.window.geometry('+800+300')

        # Create data
        self.label1 = tkinter.Label(self.window, text='代號:')
        self.entry1 = tkinter.Entry(self.window, width=15)

        self.label2 = tkinter.Label(self.window, text='名稱:')
        self.entry2 = tkinter.Entry(self.window, width=15)

        self.label3 = tkinter.Label(self.window, text='性質:')
        self.entry3 = tkinter.Entry(self.window, width=15)

        self.label4 = tkinter.Label(self.window, text='人數:')
        self.entry4 = tkinter.Entry(self.window, width=15)

        self.label5 = tkinter.Label(self.window, text='社課時間:')
        self.entry5 = tkinter.Entry(self.window, width=15)

        self.label6 = tkinter.Label(self.window, text='社辦:')
        self.entry6 = tkinter.Entry(self.window, width=15)

        self.label7 = tkinter.Label(self.window, text='介紹:')
        self.entry7 = tkinter.Text(self.window, width=20)

        # 排位置

        self.label1.grid(row=1, column=1, sticky="E")
        self.entry1.grid(row=1, column=2, padx=5, pady=5)

        self.label2.grid(row=2, column=1, sticky="E")
        self.entry2.grid(row=2, column=2, padx=5, pady=5)

        self.label3.grid(row=3, column=1, sticky="E")
        self.entry3.grid(row=3, column=2, padx=5, pady=5)

        self.label4.grid(row=4, column=1, sticky="E")
        self.entry4.grid(row=4, column=2, padx=5, pady=5)

        self.label5.grid(row=5, column=1, sticky="E")
        self.entry5.grid(row=5, column=2, padx=5, pady=5)

        self.label6.grid(row=6, column=1, sticky="E")
        self.entry6.grid(row=6, column=2, padx=5, pady=5)

        self.label7.grid(row=7, column=1, sticky="E")
        self.entry7.grid(row=7, column=2, padx=5, pady=5)

        # Create buttons
        self.button = tkinter.Button(self.window, text='完成', command=self.add_club)

        self.button.grid(row=8, padx=5, pady=5, column=2, sticky="E")

        tkinter.mainloop()

    def add_club(self):
        # Get the data.

        club_dic = load_info(FILENAME)

        code = self.entry1.get()
        name = self.entry2.get()
        kind = self.entry3.get()
        num = self.entry4.get()
        time = self.entry5.get()
        loca = self.entry6.get()
        intro = self.entry7.get(1.0, tkinter.END)

        club_dic[code] = (name, kind, num, time, loca, intro)

        save_info(FILENAME, club_dic)

        self.window.destroy()
