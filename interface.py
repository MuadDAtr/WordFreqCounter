import tkinter as tk

class FreqQUI:
    def __init__(self):
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text = "Word Frequency Counter", font = ('Times New Roman', 18))
        self.label.pack(padx = 20, pady =20)

        self.textbox = tk.Text(self.root, height = 10, font = ('Arial', 12))
        self.textbox.pack(padx = 10)

        self.button = tk.Button(self.root, text = "Count", font = ('Arial', 14))
        self.button.pack(padx = 10, pady = 10)

        

        self.root.mainloop()

    def show_message:
        

FreqQUI()