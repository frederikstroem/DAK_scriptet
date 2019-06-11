import tkinter as tk

class DAKScreen:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("DAK_scriptet")
        self.tk.attributes("-fullscreen", True)
        self.frame = tk.Frame(self.tk)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.tk.bind("<Escape>", self.quit)

    def quit(self, event=None):
        self.tk.destroy()

if __name__ == '__main__':
    window = DAKScreen()
    window.tk.mainloop()
