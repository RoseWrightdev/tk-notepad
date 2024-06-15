import tkinter as tk
import os


class NoteApp:
    def __init__(self):
        self.root = self.create_window()
        self.left_frame = self.create_frame(self.root, "left")
        self.right_frame = self.create_frame(self.root, "right")
        self.saved_notes_dir = "notes"
        self.text_box = self.create_text_box()
        self.text_box_label = self.create_text_box_label()
        self.saved_files_list = self.create_saved_files_list()
        self.save_button = self.create_save_button()
        self.update_saved_files_list()
        self.root.mainloop()

    @staticmethod
    def create_window():
        root = tk.Tk()
        root.state("zoomed")
        root.title("Rose Notes")
        return root

    @staticmethod
    def create_frame(root, pos: str):
        if pos == "left":
            frame = tk.Frame(root, width=200)
        else:
            frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        return frame

    def create_text_box(self):
        text_box = tk.Text(self.right_frame, font=("Arial", 12))
        text_box.pack(fill=tk.BOTH, expand=True)
        return text_box

    def create_text_box_label(self):
        text_box_label = tk.Label(self.right_frame, text="untitled - note")
        text_box_label.pack()
        return text_box_label

    def create_saved_files_list(self):
        saved_files_list = tk.Listbox(self.left_frame)
        saved_files_list.pack(fill=tk.BOTH, expand=True)
        return saved_files_list

    def create_save_button(self):
        save_button = tk.Button(self.left_frame, text="Save", command=self.save)
        save_button.pack()
        return save_button

    def get_file_name(self):
        text_content = self.text_box.get("1.0", tk.END)
        title_start = text_content.find("# ")

        if title_start != -1:  # Check if "#" and space are found
            # Extract the title (up to 32 chars or newline)
            title = text_content[title_start + 2:min(title_start + 32, text_content.find("\n"))].replace("\n", "")
        else:
            # use first 16 chars as title
            title_from_content = text_content[:min(16, len(text_content))]
            title = title_from_content.rstrip("\n")  # Remove trailing newline
        return title + ".md"

    def save(self):
        text_content = self.text_box.get("1.0", tk.END)

        # check that saves folder exists
        if not os.path.exists(self.saved_notes_dir):
            os.makedirs(self.saved_notes_dir)

        # file path
        file_name = self.get_file_name()
        file_path = os.path.join(self.saved_notes_dir, file_name)

        # check if file of the same name exists
        if os.path.exists(file_path):
            # Handle file already exists scenario (e.g., show a warning)
            print("File already exists!")
        else:
            with open(file_path, "w") as file:
                file.write(text_content)
            print("Text saved to ", file_path)

    def update_saved_files_list(self):
        if os.path.exists(self.saved_notes_dir):
            for filename in os.listdir(self.saved_notes_dir):
                if filename.endswith(".md"):
                    self.saved_files_list.insert(tk.END, filename)


if __name__ == "__main__":
    app = NoteApp()
