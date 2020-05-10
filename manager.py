import tkinter
import tkinter.messagebox
from functools import partial

from load_save import load_info
from load_save import save_info

FILENAME = 'ClubInfo.dat'


def ClubInfoGUI(code):
    club_dic = load_info(FILENAME)

    # Create window
    window = tkinter.Tk(className="社團資訊系統")
    window.geometry('+800+300')

    # Create data
    label1 = tkinter.Label(window, text='代號:')
    label1_1 = tkinter.Label(window, width=15, text=code)

    label2 = tkinter.Label(window, text='名稱:')
    entry2 = tkinter.Entry(window, width=15)
    entry2.insert(tkinter.END, club_dic[code][0])
    print(club_dic[code][0])

    label3 = tkinter.Label(window, text='性質:')
    entry3 = tkinter.Entry(window, width=15)
    entry3.insert(tkinter.END, club_dic[code][1])
    print(club_dic[code][1])
    print(club_dic[code])

    label4 = tkinter.Label(window, text='人數:')
    entry4 = tkinter.Entry(window, width=15)
    entry4.insert(tkinter.END, club_dic[code][2])
    print(club_dic[code][2])

    label5 = tkinter.Label(window, text='社課時間:')
    entry5 = tkinter.Entry(window, width=15)
    entry5.insert(tkinter.END, club_dic[code][3])
    print(club_dic[code][3])

    label6 = tkinter.Label(window, text='社辦:')
    entry6 = tkinter.Entry(window, width=15)
    entry6.insert(tkinter.END, club_dic[code][4])
    print(club_dic[code][4])

    label7 = tkinter.Label(window, text='介紹:')
    entry7 = tkinter.Text(window, width=20)
    entry7.insert(1.0, club_dic[code][5])
    # 排位置

    label1.grid(row=1, column=1, sticky="E")
    label1_1.grid(row=1, column=2, padx=5, pady=5)

    label2.grid(row=2, column=1, sticky="E")
    entry2.grid(row=2, column=2, padx=5, pady=5)

    label3.grid(row=3, column=1, sticky="E")
    entry3.grid(row=3, column=2, padx=5, pady=5)

    label4.grid(row=4, column=1, sticky="E")
    entry4.grid(row=4, column=2, padx=5, pady=5)

    label5.grid(row=5, column=1, sticky="E")
    entry5.grid(row=5, column=2, padx=5, pady=5)

    label6.grid(row=6, column=1, sticky="E")
    entry6.grid(row=6, column=2, padx=5, pady=5)

    label7.grid(row=7, column=1, sticky="E")
    entry7.grid(row=7, column=2, padx=5, pady=5)

    # Create buttons
    button1 = tkinter.Button(window, text='修改',
                             command=partial(save_edit, club_dic, code, entry2,
                                             entry3, entry4, entry5, entry6, entry7))

    button2 = tkinter.Button(window, text='關閉',
                             command=window.destroy)

    button1.grid(row=8, padx=5, pady=5, column=2, sticky="E")
    button2.grid(row=8, padx=5, pady=5, column=1, sticky="E")

    tkinter.mainloop()


########################################################

def save_edit(club_dic, code, entry2, entry3, entry4, entry5, entry6, entry7):
    new_name = entry2.get()
    new_kind = entry3.get()
    new_num = entry4.get()
    new_time = entry5.get()
    new_loca = entry6.get()
    new_intro = entry7.get(1.0, tkinter.END)

    print(new_name, new_kind, new_num, new_time, new_loca, new_intro)

    club_dic[code] = (new_name, new_kind, new_num, new_time,
                      new_loca, new_intro)

    print(club_dic[code])

    tkinter.messagebox.showinfo(title='完成', message='修改已儲存！')

    FILENAME = 'ClubInfo.dat'
    save_info(FILENAME, club_dic)
