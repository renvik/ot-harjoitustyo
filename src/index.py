from tkinter import Tk
from ui.ui import UI

def main():
    """the class launches the UI and imports tkinter tk
    """
    window = Tk()
    window.title("Information about trains")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
