import tkinter as tk
import os

# window setup
root = tk.Tk()
root.state("zoomed")
root.title("Rose Notes")
saved_notes_dir = "notes"

# define width for left frame
left_frame_width = 200

# create main frames
left_frame = tk.Frame(root, width=left_frame_width)
right_frame = tk.Frame(root)

# pack the frames horizontally
left_frame.pack(side=tk.LEFT, fill=tk.Y)
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# function to get file name
def get_file_name():
    text_content = text_box.get("1.0", tk.END)
    title_start = text_content.find("# ")

    if title_start != -1:  # Check if "#" and space are found
        # Extract the title (up to 32 chars or newline)
        title = text_content[title_start + 2:min(title_start + 32, text_content.find("\n"))].replace("\n", "")
    else:
        # use first 16 chars as title
        title_from_content = text_content[:min(16, len(text_content))]
        title = title_from_content.rstrip("\n")  # Remove trailing newline
    return title + ".md"

# function to save
def save():
    text_content = text_box.get("1.0", tk.END)

    # check that saves folder exists
    if not os.path.exists(saved_notes_dir):
        os.makedirs(saved_notes_dir)

    # file path
    file_name = get_file_name()
    file_path = os.path.join(saved_notes_dir, file_name)

    # check if file of the same name exists
    if os.path.exists(file_path):
        raise Exception("There is already a file with that name")
    else:
        with open(file_path, "w") as file:
            file.write(text_content)
        print("Text saved to ", file_path)

    update_saved_files_list()
    return


# save button setup
save_button = tk.Button(left_frame, text="Save", command=save)
save_button.pack()

# listbox setup for saved files
saved_files_list = tk.Listbox(left_frame)
saved_files_list.pack(fill=tk.BOTH, expand=True)


# function to update list of saved files
def update_saved_files_list():
    if os.path.exists(saved_notes_dir):
        for filename in os.listdir(saved_notes_dir):
            if filename.endswith(".md"):
                saved_files_list.insert(tk.END, filename)


update_saved_files_list()  # call update function on startup

# text box setup
text_box = tk.Text(right_frame, font=("Arial", 12))
text_box.pack(fill=tk.BOTH, expand=True)

root.mainloop()
