import tkinter
import tkinter.messagebox

from load_save import load_info
from load_save import save_info

FILENAME = 'ClubInfo.dat'


class DeleteGUI:
    def __init__(self):
        # Create window
        self.window = tkinter.Tk(className="社團資訊系統")
        self.window.geometry('+800+300')

        # original data
        self.label = tkinter.Label(self.window, text='請輸入欲刪除社團代碼:')
        self.entry = tkinter.Entry(self.window, width=15, )

        self.label.grid(row=1, column=2)
        self.entry.grid(row=1, column=3, padx=5, pady=5)
        # Create buttons
        self.button = tkinter.Button(self.window, text='刪除', command=self.remind)

        self.quit_button = tkinter.Button(self.window, text='結束', command=self.window.destroy)

        self.button.grid(row=2, padx=5, pady=5, column=3, sticky="E")
        self.quit_button.grid(row=2, padx=5, pady=5, column=2)

        tkinter.mainloop()

    def remind(self):

        msgbox = tkinter.messagebox.askquestion(title='注意', message='確定刪除？')

        if msgbox == 'yes':
            self.delete()

    def delete(self):

        club_dic = load_info(FILENAME)

        code = self.entry.get()

        if code in club_dic:
            del club_dic[code]
            tkinter.messagebox.showinfo(title='完成', message='已刪除')

            save_info(FILENAME, club_dic)

        else:
            tkinter.messagebox.showinfo(title='注意', message='該社團不存在')
