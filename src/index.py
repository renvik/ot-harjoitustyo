from tkinter import Tk
from ui.ui import UI
# this class launches the UI

def main():

    window = Tk()
    window.title("Information about trains")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
