from tkinter import ttk, constants

class ResultsView:
    def __init__(self, root, results):
        self._root = root
        self._frame = None
        self._results = results

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
     
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Train information is currently shown in the terminal")

        label.grid(row=0, column=0)