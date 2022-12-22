from tkinter import ttk, constants
from services.train_service import TrainService

class SearchView:
    """the view is responsible for showing the search form"""

    def __init__(self, root, show_results):
        """_summary_

        Args:
            root:
                TKinter-element into which the user interface is initialized
        """
        self._root = root
        self._frame = None
        self.train_service = TrainService()
        self._initialize_search_form()
        self._show_results = show_results

    def pack(self):
        """shows the view"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """destroys the view"""
        self._frame.destroy()

    def _handle_button_click(self):
        entry_value = self.train_entry.get()
        departure_date = self.date_entry.get()
        print(f"Value of train number and date: {entry_value} and {departure_date}")
        data = self.train_service.get_train(entry_value, departure_date)
        self._show_results(data)

    def _initialize_search_form(self):
        self._frame = ttk.Frame(master=self._root)
        
        heading_label = ttk.Label(master=self._frame, text="Train information")
        train_label = ttk.Label(master=self._frame, text="Train number")
        self.train_entry = ttk.Entry(master=self._frame)
        date_label = ttk.Label(master=self._frame, text="Departure date (YYYY-MM-DD)")
        self.date_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(
             master=self._frame,
             text="Search",
             command=self._handle_button_click)
    
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        train_label.grid(padx=5, pady=5)
        date_label.grid(padx=5, pady=5)

        self.train_entry.grid(row=1, column=1, sticky=(
             constants.E, constants.W), padx=5, pady=5)
        self.date_entry.grid(row=2, column=1, sticky=(
             constants.E, constants.W), padx=5, pady=5)     
        button.grid(columnspan=2, sticky=(
             constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
        



