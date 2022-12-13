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
        x = {
        "departureDate": 2022-12-13,
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Train information will be shown here in the future releases"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
        }
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=x["children"])

        label.grid(row=0, column=0)