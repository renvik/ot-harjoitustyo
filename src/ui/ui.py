from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Train information")

        train_label = ttk.Label(master=self._root, text="Train number")
        train_entry = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="Search")

        heading_label.grid(row=0, column=0, columnspan=2)

        train_label.grid(row=1, column=0)
        train_entry.grid(row=1, column=1)

        button.grid(row=3, column=0, columnspan=2)

        self._root.grid_columnconfigure(1, weight=1)
        
window = Tk()
window.title("Information about trains")

ui = UI(window)
ui.start()

window.mainloop()