import tkinter.messagebox
from tkinter import *

import club_GUI_add
import club_GUI_delete
from load_save import load_info

FILENAME = 'ClubInfo.dat'


class DeveloperGUI:

    def __init__(self):
        window = Tk()
        window.title("社團資訊系統")
        window.geometry('+800+300')

        button_add = Button(window, text='新增社團', command=club_GUI_add.AddClubInfoGUI)
        button_delete = Button(window, text='刪除社團', command=club_GUI_delete.DeleteGUI)
        button_show_all = Button(window, text='顯示所有社團', command=self.showall)
        quit_button = Button(window, text='結束', command=window.destroy)

        button_add.grid(row=1, column=2, padx=5, pady=5)
        button_delete.grid(row=2, column=2, padx=5, pady=5)
        button_show_all.grid(row=3, column=2, padx=5, pady=5)
        quit_button.grid(row=4, column=2, padx=5, pady=5)

        mainloop()

    def showall(self):
        club_dic = load_info(FILENAME)
        name_lst = []

        for code in club_dic:
            text = code + ' ' + club_dic[code][0]
            print(text)
            name_lst.append(text)

        tkinter.messagebox.showinfo(title='所有社團', message=name_lst)
