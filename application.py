import tkinter
from tkinter import ttk

_verbose = True
_pad = 5


class Application(tkinter.Frame):
    def __init__(self, master=None, left_name="Left", right_name="Right", on_left_callback=None, on_right_callback=None):
        super().__init__(master)

        master.bind("<Left>", self.on_left_key)
        master.bind("<Right>", self.on_right_key)

        self.mainFrame = tkinter.Frame(master)
        self.mainFrame.pack(fill=tkinter.BOTH, expand=True, padx=_pad, pady=_pad)

        # self.canvas = Canvas(master, width=300, height=300)
        self.canvas = tkinter.Canvas(self.mainFrame)
        self.canvas.pack(side=tkinter.TOP, anchor=tkinter.S, fill=tkinter.BOTH, expand=True, padx=(_pad, 0))

        self.swipeButtonFrame = tkinter.Frame(master, height=5)
        self.swipeButtonFrame.pack(side=tkinter.TOP, anchor=tkinter.S, pady=(0, 20))

        self.button_left = ttk.Button(self.swipeButtonFrame, style="W.TButton", text=left_name, command=self.on_left)
        self.button_left.pack(fill=tkinter.BOTH, padx=(_pad * 2, 0), expand=True, side=tkinter.LEFT, anchor=tkinter.W)
        self.on_left_callback = on_left_callback

        self.button_right = ttk.Button(self.swipeButtonFrame, style="W.TButton", text=right_name, command=self.on_right)
        self.button_right.pack(fill=tkinter.BOTH, padx=(_pad * 2, 0), expand=True, side=tkinter.RIGHT, anchor=tkinter.E)
        self.on_right_callback = on_right_callback

        self.master = master
        self.pack()

    def on_left_key(self, event):
        if _verbose:
            print("on_left_key()")
        self.on_left()

    def on_left(self):
        if _verbose:
            print("on_left()")

        if self.on_left_callback is not None:
            self.on_left_callback()

    def on_right_key(self, event):
        if _verbose:
            print("on_right_key()")
        self.on_right()

    def on_right(self):
        if _verbose:
            print("on_right()")

        if self.on_right_callback is not None:
            self.on_right_callback()


root = tkinter.Tk()

# <editor-fold desc="Setup Window Size">
_screen_width = root.winfo_screenwidth()
_screen_height = root.winfo_screenheight()
_width = int(_screen_width / 2)
_height = int(_screen_height / 2)
_x = int(_width / 2)
_y = int(_height / 2)
root.geometry("{}x{}+{}+{}".format(_width, _height, _x, _y))
# </editor-fold>

# <editor-fold desc="Apply Styles">
# root.configure(background=background_color, takefocus=True)
# </editor-fold>
