import tkinter as tk
import os

# window setup
root = tk.Tk()
root.state("zoomed")
root.title("Rose Notes")

# frame setup
frm = tk.Frame(root)
frm.grid()
frm.pack(fill=tk.BOTH, expand=True)



def get_file_name():
    text_content = text_box.get("1.0", tk.END)

    # Find the first occurrence of "#" followed by a space
    title_start = text_content.find("# ")

    if title_start != -1:  # Check if "#" and space are found
        # Extract the title (up to 32 chars or newline)
        title = text_content[title_start + 2:min(title_start + 32, text_content.find("\n"))].replace("\n", "")
    else:
        # use first 16 chars as titled
        title_from_content = text_content[:min(16, len(text_content))]
        title = title_from_content.rstrip("\n")  # Remove trailing newline
    return title + ".md"


def save():
    text_content = text_box.get("1.0", tk.END)
    saved_notes_dir = "notes"

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
    return


save_button = tk.Button(frm, text="Save", command=save)
save_button.pack()

# text box setup
text_box = tk.Text(frm, font=("Arial", 12, "anti"))
text_box.pack(fill=tk.BOTH, expand=True)

root.mainloop()
