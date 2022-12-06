from tkinter import ttk, constants

class TrainInfo:
    def __init__(self, root, traininfo): # constructor for the class, instantiates an UI-object
        self._root = root
        self.train_info = traininfo
        self._partview = None

        self._initialize()
        
    def destroy(self):
        self._partview.destroy()

    def pack(self):
        self._partview.pack(fill=constants.X)

    def _initialize(self):
        self._partview = ttk.Frame(master=self._root)
