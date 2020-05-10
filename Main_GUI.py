import tkinter

import de_login
import ma_login
import student

FILENAME = 'ClubInfo.dat'


class MyGUI:

    def __init__(self):
        window = tkinter.Tk()
        window.title("社團資訊系統")
        window.geometry('180x100+500+300')

        label = tkinter.Label(window, text='我是')

        button_developer = tkinter.Button(window, text='管理員',
                                          command=de_login.LoginGUI)
        button_student = tkinter.Button(window, text='學生',
                                        command=student.Choose_clubGUI)
        button_manager = tkinter.Button(window, text='社團幹部',
                                        command=ma_login.LoginGUI)
        quit_button = tkinter.Button(window, text='結束',
                                     command=window.destroy)

        label.grid(row=1, column=2, padx=5, pady=5)
        button_developer.grid(row=3, column=3, padx=5, pady=5)
        button_student.grid(row=3, column=1, padx=5, pady=5)
        button_manager.grid(row=3, column=2, padx=5, pady=5)
        quit_button.grid(row=4, column=2, padx=5, pady=5)

        tkinter.mainloop()


my_gui = MyGUI()
