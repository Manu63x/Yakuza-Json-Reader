from tkinter import *
from tkinter.filedialog import askopenfilename
from jsonfunctions import *

def save():
    #Code to be written
    pass
 
def load():
    global filename
    filename = askopenfilename()
    f = open(filename)
    data = json.load(f)
    for i in range(1, getItemsNumber(filename)):
        a = json.dumps(data['' + str(i)])
        for key in json.loads(a):
            objCat = data['' + str(i)]['' + key]['category']
            if(objCat == 2 or objCat == 3 or objCat == 4 or objCat == 5 or objCat == 6 or objCat == 7):
                mylist.insert(END, str(i)) 
    mylist.pack(side="left", fill="both", expand=True)
    f.close()
    pass

def loadItemIntoText(event): 
    cs = mylist.curselection()
    selected = mylist.get(cs)
    # print(selected)
    # TODO: insert text into TEXT areas with getName and Explanation by Id function
    
filename = ''

root = Tk()
root.title("Yakuza Kiwami 2 JSON Reader")
root.state('zoomed')

# Frame principale
main_frame = Frame(root)
main_frame.pack(fill="both", expand=True)

# Pannello sinistro
left_panel = PanedWindow(main_frame, bd=4, relief="raised", bg="red")
left_panel.pack(side="left", fill="both", expand=False)

# Lista
mylist = Listbox(left_panel)  
mylist.bind('<Double-1>', loadItemIntoText)

# Scrollbar
myscroll = Scrollbar(left_panel, orient=VERTICAL, command=mylist.yview) 
myscroll.pack(side="right", fill="y") 
mylist.config(yscrollcommand=myscroll.set)

# Pannello destro
right_panel = PanedWindow(main_frame, bd=4, relief="raised", bg="blue")
right_panel.pack(side="right", fill="both", expand=True)

# Text Area
text1 = Text(right_panel)
text1.pack(fill="both", expand=True)
text2 = Text(right_panel)
text2.pack(fill="both", expand=True)

# Menu
mainmenu = Menu(root)
mainmenu.add_command(label="Load", command=load)
mainmenu.add_command(label="Save", command=save)  
mainmenu.add_command(label="Exit", command=root.destroy)
root.config(menu=mainmenu)

root.mainloop()
