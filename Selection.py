from tkinter import filedialog
from tkinter import *


def add_file():
    text = filedialog.askopenfilename(initialdir="/", title="Select file",
                                      filetypes=(("jpeg files", "*.jpg"),
                                                 ("bmp files", "*.bmp"),
                                                 ("png files", "*.png")
                                                 #("all files", "*.*")
                                                 ))
    listbox.insert(END, text)

def del_file():
    select = list(listbox.curselection())
    select.reverse()
    for i in select:
        listbox.delete(i)

def next_action():
    arr_path = []
    num_photo = listbox.size()
    for path in range(0, num_photo):
        arr_path.append(listbox.get(path))
    select_window.destroy()


select_window = Tk()

select_window.title("Select files to edit.")  # PixelMaker
select_window.geometry('305x200')  # '800x600'

listbox = Listbox(select_window)
listbox.grid(column=0, row=0, rowspan=3, sticky=W + E + N + S, ipadx=50, ipady=20)

btn_add = Button(select_window, text="Add a file", command=add_file)
btn_add.grid(column=1, row=0, sticky=W + E + N + S)

btn_del = Button(select_window, text="Delete the file", command=del_file)
btn_del.grid(column=1, row=1, sticky=W + E + N + S)

btn_next = Button(select_window, text="Next step", command=next_action)
btn_next.grid(column=0, row=2, columnspan=2, sticky=W + E + N + S)

select_window.mainloop()
