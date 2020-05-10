import tkinter
import tkinter.messagebox
import developer_GUI


class LoginGUI:
    def __init__(self):
        # Create window
        self.window = tkinter.Tk(className="社團資訊系統")
        self.window.geometry('+600+300')

        # original data
        self.label = tkinter.Label(self.window, text='請輸入密碼:')
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

        if code == '0000':
            developer_GUI.DeveloperGUI()

        else:
            tkinter.messagebox.showerror(title='錯誤', message='密碼錯誤！')
