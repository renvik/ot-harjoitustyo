from tkinter import Tk, ttk, constants
from services.train_service import TrainService
# UI:ssa tulee alustaa service-olio

class UI:
    def __init__(self, root):
    #def __init__(self, root, train_service):
        self._root = root
        self.entry = None
        self.train_service = TrainService()

    def start(self):
        #self.entry = ttk.Entry(master=self._root) # buttonia varten
        
        heading_label = ttk.Label(master=self._root, text="Train information")
        train_label = ttk.Label(master=self._root, text="Train number")
        self.train_entry = ttk.Entry(master=self._root)
        button = ttk.Button(
            master=self._root, 
            text="Search",
            command=self._handle_button_click)

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        train_label.grid(padx=5, pady=5)
        
        self.train_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)
    # tapahtuman käsittelijä - toimii tämä entry value pitäisi antaa
    def _handle_button_click(self):
        entry_value = self.train_entry.get() #junan numero
        print(f"Value of entry is: {entry_value}")
        self.train_service.get_train(entry_value)
        

window = Tk()
window.title("Information about trains")

ui = UI(window)
ui.start()

window.mainloop()