from tkinter import Tk, ttk, constants
from services.train_service import TrainService
#from ui.train_info import TrainInfo
from ui.test_view import TestView

class UI:
    def __init__(self, root): # constructor for the class, instantiates an UI-object
        self._root = root
        #self._frame = None
        #self.entry = None
        self.train_service = TrainService()
        self._current_view = None
        #self.train_info_frame = None

    def start(self): # renders the UI
        self._frame = ttk.Frame(master=self._root)
        # starts train_info view:
        self.train_info_frame = ttk.Frame(master=self._frame)
        
        heading_label = ttk.Label(master=self._root, text="Train information")
        train_label = ttk.Label(master=self._root, text="Train number")
        self.train_entry = ttk.Entry(master=self._root)
        button = ttk.Button(
            master=self._root,
            text="Search",
            command=self._handle_button_click)

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        train_label.grid(padx=5, pady=5)

        self.train_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        #self.train_info_frame

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
        
    # event handler: takes the train number input and passes entry to the train_service
    def _handle_button_click(self):
        entry_value = self.train_entry.get()  # train number input from the user
        print(f"Value of entry is: {entry_value}")
        self._show_test_view()
        #traininfo = self.train_service.get_train(entry_value) # passes value to the TrainService -class
        #self.initialize_train_info(traininfo)
    def _handle_hello_world(self):
        print("Hello World")

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_test_view(self):
        self._hide_current_view()
        self._current_view = TestView(
            self._root,
            self._show_test_view,
            self._handle_hello_world
        )
        self._current_view.pack()

 #   def initialize_train_info(self, traininfo):
 #       if self.train_info_frame:
 #           self.train_info_frame.destroy()
 #       self.train_info_frame = TrainInfo(self.train_info_frame, traininfo)
 #       self.train_info_frame.pack()