import tkinter
from tkinter import ttk

pad = 5
background_color = "#2b2b2b"
interaction_color = "#4e5052"
label_color = "#b4b4b4"
_verbose = True
_style = None


class Application(tkinter.Frame):
    def __init__(self, master=None, left_name="Left", right_name="Right", on_left_callback=None, on_right_callback=None):
        super().__init__(master)

        master.bind("<Left>", self.on_left_key)
        master.bind("<Right>", self.on_right_key)

        self.mainFrame = tkinter.Frame(master, background=background_color)
        self.mainFrame.pack(fill=tkinter.BOTH, expand=True, padx=pad, pady=pad)

        self.canvas = tkinter.Canvas(self.mainFrame, background=background_color, highlightbackground=background_color)
        self.canvas.pack(side=tkinter.TOP, anchor=tkinter.S, fill=tkinter.BOTH, expand=True, padx=(pad, 0))

        self.swipeButtonFrame = tkinter.Frame(master, height=5, background=background_color)
        self.swipeButtonFrame.pack(side=tkinter.TOP, anchor=tkinter.S, pady=(0, 20))

        self.button_left_string_var = tkinter.StringVar()
        self.button_left_string_var.set(left_name)
        self.button_left = ttk.Button(self.swipeButtonFrame, style="W.TButton",
                                      textvariable=self.button_left_string_var, command=self.on_left)
        self.button_left.pack(fill=tkinter.BOTH, padx=(pad * 2, 0), expand=True, side=tkinter.LEFT, anchor=tkinter.W)
        self.on_left_callback = on_left_callback

        self.button_right_string_var = tkinter.StringVar()
        self.button_right_string_var.set(right_name)
        self.button_right = ttk.Button(self.swipeButtonFrame, style="W.TButton",
                                       textvariable=self.button_right_string_var, command=self.on_right)
        self.button_right.pack(fill=tkinter.BOTH, padx=(pad * 2, 0), expand=True, side=tkinter.RIGHT, anchor=tkinter.E)
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


def initiate_style(root_widget):
    if _verbose:
        print("initiate_style")

    global _style
    _style = ttk.Style(root_widget)
    _style.configure("W.TButton", background=background_color, foreground=label_color,
                     highlightbackground=background_color, highlightthickness=0)
    # _style.configure("Black.TLabelframe", foreground="black", background="white")

    # https://www.tcl.tk/man/tcl8.6/TkCmd/ttk_combobox.htm
    # set tkk combo box style
    combobox_style = ttk.Style(root_widget)
    combobox_style.theme_create("combostyle", parent="alt",
                                settings={
                                    "TCombobox": {
                                        "configure": {
                                            "arrowcolor": interaction_color,
                                            "background": background_color,
                                            "bordercolor": background_color,
                                            "darkcolor": background_color,
                                            "focusfill": background_color,
                                            "foreground": background_color,
                                            "fieldbackground": background_color,
                                            "lightcolor": background_color,
                                            "selectbackground": background_color,
                                            "selectforeground": label_color,
                                        }
                                    }
                                })
    combobox_style.theme_use("combostyle")

    # the is the actual dropdown
    combobox_style.master.option_add("*TCombobox*Listbox.background", background_color)
    combobox_style.master.option_add("*TCombobox*Listbox.foreground", label_color)
    combobox_style.master.option_add("*TCombobox*Listbox.selectBackground", background_color)
    combobox_style.master.option_add("*TCombobox*Listbox.selectForeground", label_color)


def set_icon(root_widget):
    return
    if _verbose:
        print_new_line("set_icon")
    # project_dir = get_parent_dir(os.path.realpath(__file__), 2)
    # icon_path = os.path.join(project_dir, "icons/icon.png")
    # print icon_path
    # root.wm_iconbitmap(icon_path)
    # photo = PhotoImage(file="icon.png")
    # # root.iconphoto(True, photo)
    # root.tk.call('wm', 'iconphoto', root._w, photo)
    root_widget.iconbitmap("icons/icon.icns")
    # root.tk.call('wm', 'iconphoto', root._w, img)


def _get_style():
    return _style


root = tkinter.Tk()
initiate_style(root)

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
root.configure(background=background_color, takefocus=True)
# </editor-fold>


style = property(_get_style)
