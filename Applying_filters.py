from PIL import Image, ImageDraw
from datetime import datetime, date, time
from tkinter import *

apply_window = Tk()

apply_window.title("Select a filter for each photo.")
apply_window.geometry('800x600')  # '800x600'







# Negative.
btn_neg = Button(apply_window, text="Add a file", command=negative)
btn_neg.grid(column=1, row=0, sticky=W + E + N + S)
# Grayscale.
btn_gray = Button(apply_window, text="Add a file", command=gray)
btn_gray.grid(column=1, row=0, sticky=W + E + N + S)
# Sepia.
btn_sepia = Button(apply_window, text="Add a file", command=sepia)
btn_sepia.grid(column=1, row=0, sticky=W + E + N + S)
# Brightness changes.
btn_bright = Button(apply_window, text="Add a file", command=add_file)
btn_bright.grid(column=1, row=0, sticky=W + E + N + S)
# Contrast.
btn_contrast = Button(apply_window, text="Add a file", command=add_file)
btn_contrast.grid(column=1, row=0, sticky=W + E + N + S)
# Black and white.
btn_BandW = Button(apply_window, text="Add a file", command=add_file)
btn_BandW.grid(column=1, row=0, sticky=W + E + N + S)
# Adding noise.
btn_noise = Button(apply_window, text="Add a file", command=add_file)
btn_noise.grid(column=1, row=0, sticky=W + E + N + S)

apply_window.mainloop()
