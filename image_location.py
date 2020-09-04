from PIL import Image, ImageTk
from application import *
from pythonutils.os_utils import *
import shutil

_verbose = True
# input_files = stripped_input("File Directory: ")
input_files = "/Users/georgekatsaros/Desktop/Test/Files"
# input_swipe_left_destination = stripped_input("Swipe Left Directory: ")
input_swipe_left_destination = "/Users/georgekatsaros/Desktop/Test/Keep"
swipe_left_destination_name = os.path.basename(input_swipe_left_destination)
# input_swipe_right_destination = stripped_input("Swipe Right Directory: ")
input_swipe_right_destination = "/Users/georgekatsaros/Desktop/Test/To Delete"
swipe_right_destination_name = os.path.basename(input_swipe_right_destination)
file_paths = []
file_path_index = 0
image = None


def ensure_input_is_dir(target_input_path):
    if _verbose:
        print(f"ensure_input_is_dir( target_input_path: {target_input_path} )")

    if not os.path.isdir(target_input_path):
        print(f"{target_input_path} is not a directory!")
        exit()


def to_left():
    if _verbose:
        print("to_left")

    image_file_path = file_paths[file_path_index]
    image_file_name = os.path.basename(image_file_path)
    new_path = os.path.join(input_swipe_left_destination, image_file_name)
    shutil.move(image_file_path, new_path)
    load_next_image()


def to_right():
    if _verbose:
        print("to_right")


def load_image(image_path):
    if _verbose:
        print(f"load_image( image_path: {image_path} )")


def load_next_image():
    if _verbose:
        print("load_next_image")

    global file_paths
    global file_path_index
    file_path_index += 1

    file_path_count = len(file_paths)
    if file_path_index >= file_path_count or file_path_count == 0:
        print(f"file_path_index: {file_path_index} | file_path_count: {file_path_count}")
        exit()
    else:
        next_image = file_paths[file_path_index]

        if _verbose:
            print(f"load_next_image() | next_image: {next_image}")

        global image
        image = ImageTk.PhotoImage(file=next_image)
        app.canvas.create_image(image.width()/2, image.height()/2, image=image)


ensure_input_is_dir(input_files)
ensure_input_is_dir(input_swipe_left_destination)
ensure_input_is_dir(input_swipe_right_destination)

# recursive = yes_or_no("recursive?")
recursive = False
file_paths = get_all_in_dir(target_dir=input_files, full_path=True, recursive=recursive,
                            include_dirs=False, include_files=True)

file_path_count = len(file_paths)
print(f"file_path_index: {file_path_index} | file_path_count: {file_path_count}")
if file_path_index >= file_path_count or file_path_count == 0:
    print(f"file_path_index: {file_path_index} | file_path_count: {file_path_count}")
    exit()
else:
    for file_path in file_paths:
        print(file_path)

    app = Application(master=root, left_name=swipe_left_destination_name, right_name=swipe_right_destination_name,
                      on_left_callback=to_left, on_right_callback=to_right)
    app.master.title("Swiper: File Location")

    first_image = file_paths[file_path_index]
    image = ImageTk.PhotoImage(file=first_image)
    app.canvas.create_image(image.width()/2, image.height()/2, image=image)

    app.mainloop()
