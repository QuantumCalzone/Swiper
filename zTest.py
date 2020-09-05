from PIL import Image, ImageTk
from application import *
from pythonutils.os_utils import *
import shutil
import tkinter
from tkinter.filedialog import *


app = Application(master=root, left_name="Left", right_name="Right",
                  on_left_callback=None, on_right_callback=None)
app.master.title("Test")

app.mainloop()
