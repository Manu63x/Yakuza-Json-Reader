import os
import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, simpledialog, messagebox

class JSONTreeView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='JSON Structure', anchor='w')

        # Configure the grid
        self.grid(row=0, column=0, sticky='nsew')
        self.tree.grid(row=0, column=0, sticky='nsew')
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')

        # Configure the weights to ensure resizing
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.create_menu()
        self.json_data = None
        self.file_path = None

        # Bind double-click event to treeview
        self.tree.bind("<Double-1>", self.on_double_click)

    def create_menu(self):
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                self.json_data = json.load(f)
            self.file_path = file_path
            self.tree.delete(*self.tree.get_children())  # Clear the tree
            self.populate_tree(self.json_data)

    def save_file(self):
        if self.json_data and self.file_path:
            with open(self.file_path, 'w') as f:
                json.dump(self.json_data, f, indent=4)
            messagebox.showinfo("Success", "File saved successfully")

    def populate_tree(self, data, parent=''):
        for key, value in data.items():
            node_id = self.tree.insert(parent, 'end', text=key, open=False)
            if isinstance(value, dict):
                self.populate_tree(value, node_id)
            else:
                self.tree.insert(node_id, 'end', text=value, open=False)

    def on_double_click(self, event):
        item_id = self.tree.selection()[0]
        item_text = self.tree.item(item_id, "text")
        parent_id = self.tree.parent(item_id)

        if not parent_id:
            return  # Prevent editing root element

        if self.tree.get_children(item_id):  # if the item has children, it's a dict key
            return  # Do not allow editing dict keys directly

        # Prompt user for a new value
        new_value = simpledialog.askstring("Edit Value", f"Enter new value for {item_text}:")
        if new_value is not None:
            self.tree.item(item_id, text=new_value)
            self.update_json_data(item_id, new_value)

    def update_json_data(self, item_id, new_value):
        # Function to get the path from the root to the current item
        def get_path(item_id):
            path = []
            while item_id:
                parent_id = self.tree.parent(item_id)
                item_text = self.tree.item(item_id, "text")
                path.insert(0, item_text)
                item_id = parent_id
            return path

        # Get the path to the item being edited
        path = get_path(item_id)

        # Traverse the json_data dictionary to update the value
        data = self.json_data
        for key in path[:-1]:  # Traverse to the parent of the item
            data = data[key]
        # Update the value in the json_data dictionary
        data[path[-1]] = new_value

root = tk.Tk()
root.title("JSON Tree Viewer")
root.state('zoomed')  # Open the window in fullscreen mode
app = JSONTreeView(root)
root.mainloop()
