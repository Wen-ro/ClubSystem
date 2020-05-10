import tkinter
import tkinter.messagebox

from load_save import load_info
from manager import ClubInfoGUI

FILENAME = 'ClubInfo.dat'


class LoginGUI:
    def __init__(self):
        # Create window
        self.window = tkinter.Tk(className="社團資訊系統")
        self.window.geometry('+800+300')

        # original data
        self.label = tkinter.Label(self.window, text='請輸入社團代號:')
        self.entry = tkinter.Entry(self.window, width=15, show='*')

        self.label.grid(row=1, column=2)
        self.entry.grid(row=1, column=3, padx=5, pady=5)
        # Create buttons
        self.button = tkinter.Button(self.window, text='登入', command=self.login)
        self.quit_button = tkinter.Button(self.window, text='結束', command=self.window.destroy)

        self.button.grid(row=2, padx=5, pady=5, column=3, sticky="E")
        self.quit_button.grid(row=2, padx=5, pady=5, column=2)

        tkinter.mainloop()

    def login(self):

        code = self.entry.get()

        self.window.destroy()

        club_dic = load_info(FILENAME)

        if code in club_dic:

            ClubInfoGUI(code)

        else:
            tkinter.messagebox.showerror(title='錯誤', message='代號錯誤！')
            LoginGUI()
