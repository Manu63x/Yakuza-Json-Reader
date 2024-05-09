from tkinter import *
from tkinter import ttk

class Example:
    def __init__(self, root):
        list_1 = ['item_1', 'item_2']
        list_2 = ['a', 'b', 'c']

        for item in list_1 :
            frame = Frame(root, width=500, height=22)
            frame.pack(side=TOP, anchor=W)
            frame.propagate(0)

            Label(frame, text=item).pack(side=LEFT, anchor=W)
            entry = Entry(frame, width=11)
            entry.pack(side=RIGHT, pady=2, anchor=E)

            var = IntVar()
            var.set(0)

            sub_frame = Frame(root, relief="sunken", width=400, height=22, borderwidth=1)

            toggle_btn = ttk.Checkbutton(frame, width=2, text='+', command=lambda: self.toggle(var, toggle_btn, sub_frame),
                                     variable=var, style='Toolbutton')
            toggle_btn.pack(side=LEFT, anchor=E)

            for item in list_2:
                Label(sub_frame, text=item).pack(side=TOP)

    def toggle(self, show, toggle_button, sub_frame):
        if bool(show.get()):
            sub_frame.pack(fill="x", expand=1)
            sub_frame.propagate(1)
            toggle_button.configure(text='-')
        else:
            sub_frame.forget()
            toggle_button.configure(text='+')

def main():
    root = Tk()
    open = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()