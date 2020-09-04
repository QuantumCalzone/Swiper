from PIL import Image, ImageTk
from application import *
from pythonutils.os_utils import *
import shutil
import tkinter
from tkinter.filedialog import *

_verbose = True
file_paths = []
file_path_index = -1
image = None


def set_entry_value(entry, value):
    if _verbose:
        print(f"set_entry_value( entry: {entry.get()} , value: {value} )")

    entry.delete(0, END)
    entry.insert(0, value)


def ensure_input_is_dir(target_input_path):
    if _verbose:
        print(f"ensure_input_is_dir( target_input_path: {target_input_path} )")

    if not os.path.isdir(target_input_path):
        print(f"{target_input_path} is not a directory!")
        # exit()


def make_labeled_entry(label):
    if _verbose:
        print(f"make_labeled_entry( label: {label} )")

    input_row_frame = tkinter.Frame(master=app.canvas, height=20)
    input_row_frame.pack(side=tkinter.TOP, anchor=tkinter.N, fill=tkinter.X)

    entry_row_label = tkinter.Label(master=input_row_frame, text=label)
    entry_row_label.pack(side="left")

    entry = tkinter.Entry(master=input_row_frame)
    entry.pack(fill=tkinter.BOTH, expand=True, anchor=tkinter.E)
    entry.bind("<Button-1>", open_file)

    return entry


def open_file(event):
    if _verbose:
        print("open_file")

    destination = askdirectory(initialdir="/", title="Select a directory")
    entry = event.widget
    set_entry_value(entry, destination)


def move_file(destination):
    if _verbose:
        print(f"move_file ( destination: {destination} )")

    if file_path_index < 0:
        return

    image_file_path = file_paths[file_path_index]
    image_file_name = os.path.basename(image_file_path)
    new_path = os.path.join(destination, image_file_name)
    shutil.move(image_file_path, new_path)
    load_next_image()


def on_space(event):
    if _verbose:
        print("on_space()")
    load_next_image()


def on_delete(event):
    if _verbose:
        print("on_delete()")

    if file_path_index < 0:
        return

    os.remove(file_paths[file_path_index])
    load_next_image()


def to_left():
    if _verbose:
        print("to_left")

    move_file(input_left_destination.get())


def to_right():
    if _verbose:
        print("to_right")

    move_file(input_right_destination.get())


def start():
    if _verbose:
        print("start")

    global file_paths
    file_paths = get_all_in_dir(target_dir=input_files.get(), full_path=True, recursive=True,
                                include_dirs=False, include_files=True)
    load_next_image()


def load_next_image():
    if _verbose:
        print("load_next_image")

    swipe_left_destination_name = os.path.basename(input_left_destination.get())
    swipe_right_destination_name = os.path.basename(input_right_destination.get())

    app.button_left_string_var.set(swipe_left_destination_name)
    app.button_right_string_var.set(swipe_right_destination_name)

    ensure_input_is_dir(input_files.get())
    ensure_input_is_dir(input_left_destination.get())
    ensure_input_is_dir(input_right_destination.get())

    global file_paths
    global file_path_index
    file_path_index += 1

    file_path_count = len(file_paths)
    if file_path_index >= file_path_count or file_path_count == 0:
        print(f"file_path_index: {file_path_index} | file_path_count: {file_path_count}")
        # exit()
    else:
        next_image = file_paths[file_path_index]

        if _verbose:
            print(f"load_next_image() | next_image: {next_image}")

        global image
        image = ImageTk.PhotoImage(file=next_image)
        app.canvas.create_image(app.canvas.winfo_width()/2, app.canvas.winfo_height()/2, image=image)


app = Application(master=root, left_name="Left", right_name="Right",
                  on_left_callback=to_left, on_right_callback=to_right)
app.master.title("Swiper: File Location")

input_files = make_labeled_entry("Image Directory To Swipe: ")
input_left_destination = make_labeled_entry("Left Destination: ")
input_right_destination = make_labeled_entry("Right Destination: ")
start_button = tkinter.Button(master=app.canvas, text="Start", command=start)
start_button.pack(side=tkinter.TOP, anchor=tkinter.N, fill=tkinter.X)

# set_entry_value(input_files, "/Users/georgekatsaros/Desktop/Test/Files")
# set_entry_value(input_left_destination, "/Users/georgekatsaros/Desktop/Test/Keep")
# set_entry_value(input_right_destination, "/Users/georgekatsaros/Desktop/Test/To Delete")

app.master.bind("<space>", on_space)
app.master.bind("<BackSpace>", on_delete)
app.master.bind("<Delete>", on_delete)

app.mainloop()
