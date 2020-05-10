import tkinter
import tkinter.messagebox
from load_save import load_info
from functools import partial

FILENAME = 'ClubInfo.dat'

club_dic = load_info(FILENAME)


class Choose_clubGUI:

    def __init__(self):
        club_dic = load_info(FILENAME)

        self.main_window = tkinter.Tk(className="社團資訊系統")
        self.main_window.geometry('+800+300')

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text='選擇一個社團：')

        self.prompt_label.grid(padx=5, pady=5)

        for key in club_dic:
            self.key = tkinter.Button(self.mid_frame, text=club_dic[key][0],
                                      command=partial(self.m, key))

            self.key.grid(padx=2, pady=2)

        self.quit_button = tkinter.Button(self.bottom_frame, text='結束',
                                          command=self.main_window.destroy)

        self.quit_button.grid(padx=5, pady=5)

        self.top_frame.grid(padx=5, pady=5)
        self.mid_frame.grid(padx=5, pady=5)
        self.bottom_frame.grid(padx=5, pady=5)

        tkinter.mainloop()

    def m(self, key):
        FILENAME = 'ClubInfo.dat'

        club_dic = load_info(FILENAME)

        print(club_dic[key][0])
        tkinter.messagebox.showinfo('社團資訊',
                                    '社團名稱:' + club_dic[key][0] + '\n' + \
                                    '社團人數:' + club_dic[key][2] + '\n' + \
                                    '社團性質:' + club_dic[key][1] + '\n' + \
                                    '社課時間:' + club_dic[key][3] + '\n' + \
                                    '社辦:' + club_dic[key][4] + '\n' + \
                                    '介紹:' + club_dic[key][5])
