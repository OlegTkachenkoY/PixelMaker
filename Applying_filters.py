from datetime import datetime
from tkinter import *
from os import remove
from PIL import Image, ImageDraw, ImageTk
from tkinter import filedialog
import Filters as F


class MainClass:
    def __init__(self, master):

        self.master = master

        self.master.title("PixelMaker")
        self.master.geometry('1200x400')  # '800x600'

        self.path_image = self.resize_image(input_image_path="Examples/3.jpg", size=(280, 280))
        image = Image.open(self.path_image)
        photo = ImageTk.PhotoImage(image)

        self.frame = Frame(self.master, bd=5)
        self.frame.grid(column=0, row=9, columnspan=6, sticky=W + E + N + S)

        self.listbox = Listbox(self.master)
        self.listbox.grid(column=0, row=0, rowspan=7, sticky=W + E + N + S, ipadx=50, ipady=40)

        self.str_info = StringVar()
        self.str_info.set('Hello, this is info label. I help you.\n At start chose you photo. (Add a file)')
        self.label_info = Label(self.master,
                                textvariable=self.str_info,
                                bg='green')
        self.label_info.grid(column=0, row=7, sticky=W + E + N + S)

        self.original_photo = Canvas(self.master, height=280, width=280)
        self.original_photo.image = photo  # <--- keep reference of your image
        self.original_photo.create_image(0, 0, anchor='nw', image=photo)
        self.original_photo.grid(column=2, row=0, rowspan=9)

        self.edit_photo = Canvas(self.master, height=280, width=280)
        self.edit_photo.image = photo  # <--- keep reference of your image
        self.edit_photo.create_image(0, 0, anchor='nw', image=photo)
        self.edit_photo.grid(column=4, row=0, rowspan=9)

        self.var = IntVar()
        self.extension = 'jpg'

        self.rbutton1 = Radiobutton(self.master, text='Negative', variable=self.var, indicatoron=0, value=1,
                                    command=self.negativ_grayAction)
        self.rbutton1.grid(column=3, row=0, sticky=W + E + N + S)

        self.rbutton2 = Radiobutton(self.master, text='Gray', variable=self.var, indicatoron=0, value=2,
                                    command=self.negativ_grayAction)
        self.rbutton2.grid(column=3, row=1, sticky=W + E + N + S)

        self.rbutton3 = Radiobutton(master, text='Sepia', variable=self.var, indicatoron=0, value=3,
                                    command=self.sepiaAction)
        self.rbutton3.grid(column=3, row=2, sticky=W + E + N + S)

        self.rbutton4 = Radiobutton(master, text='Bright', variable=self.var, indicatoron=0, value=4,
                                    command=self.brightAction)
        self.rbutton4.grid(column=3, row=3, sticky=W + E + N + S)

        self.rbutton5 = Radiobutton(master, text='Contrast', variable=self.var, indicatoron=0, value=5,
                                    command=self.contrastAction)
        self.rbutton5.grid(column=3, row=4, sticky=W + E + N + S)

        self.rbutton6 = Radiobutton(master, text='Black and white', variable=self.var, indicatoron=0, value=6,
                                    command=self.black_and_whiteAction)
        self.rbutton6.grid(column=3, row=5, sticky=W + E + N + S)

        self.rbutton7 = Radiobutton(master, text='Noise', variable=self.var, indicatoron=0, value=7,
                                    command=self.noiseAction)
        self.rbutton7.grid(column=3, row=6, sticky=W + E + N + S)

        self.rbutton8 = Radiobutton(master, text='Custom', variable=self.var, indicatoron=0, value=8,
                                    command=self.customAction)
        self.rbutton8.grid(column=3, row=7, sticky=W + E + N + S)

        btn_add = Button(self.master, text="Add a file", command=self.add_file)
        btn_add.grid(column=1, row=0, rowspan=4, sticky=W + E + N + S)

        btn_del = Button(self.master, text="Delete the file", command=self.del_file)
        btn_del.grid(column=1, row=4, rowspan=4, sticky=W + E + N + S)

        btn_try = Button(self.master, text="Look at the photo", command=self.try_file)
        btn_try.grid(column=5, row=0, rowspan=4, sticky=W + E + N + S)

        btn_save = Button(self.master, text="Save", command=self.save_photo)
        btn_save.grid(column=5, row=4, rowspan=4, sticky=W + E + N + S)

        btn_jpeg = Button(self.master, text=".jpeg", command=self.jpegAction)
        btn_jpeg.grid(column=6, row=4, sticky=W + E + N + S)
        btn_jpg = Button(self.master, text=".jpg", command=self.jpgAction)
        btn_jpg.grid(column=6, row=5, sticky=W + E + N + S)
        btn_bmp = Button(self.master, text=".bmp", command=self.bmpAction)
        btn_bmp.grid(column=6, row=6, sticky=W + E + N + S)
        btn_png = Button(self.master, text=".png", command=self.pngAction)
        btn_png.grid(column=6, row=7, sticky=W + E + N + S)

    def jpegAction(self):
        self.extension = 'jpeg'
        self.str_info.set('Your photo will be saved in .jpeg format')

    def jpgAction(self):
        self.extension = 'jpg'
        self.str_info.set('Your photo will be saved in .jpg format')

    def bmpAction(self):
        self.extension = 'bmp'
        self.str_info.set('Your photo will be saved in .bmp format')

    def pngAction(self):
        self.extension = 'png'
        self.str_info.set('Your photo will be saved in .png format')

    def negativ_grayAction(self):
        self.frame.destroy()

    def sepiaAction(self):
        self.frame.destroy()

        self.frame = Frame(self.master, bg='green', bd=5)
        self.frame.grid(column=0, row=9, columnspan=6)

        label1 = Label(self.frame, text='new')
        label1.grid(column=0, row=0, sticky=W + E + N + S)
        label2 = Label(self.frame, text='60s')
        label2.grid(column=2, row=0, sticky=W + E + N + S)

        self.scale = Scale(self.frame,
                           orient=HORIZONTAL,
                           length=500,
                           from_=0, to=100,
                           tickinterval=10,
                           resolution=5)
        self.scale.grid(column=1, row=0)

    def brightAction(self):
        self.frame.destroy()

        self.frame = Frame(self.master, bg='green', bd=5)
        self.frame.grid(column=0, row=9, columnspan=6)

        label1 = Label(self.frame, text='Normal')
        label1.grid(column=0, row=0, sticky=W + E + N + S)
        label2 = Label(self.frame, text='Burning eyes')
        label2.grid(column=2, row=0, sticky=W + E + N + S)

        self.scale = Scale(self.frame,
                           orient=HORIZONTAL,
                           length=500,
                           from_=0, to=100,
                           tickinterval=10,
                           resolution=5)
        self.scale.grid(column=1, row=0)

    def contrastAction(self):
        self.frame.destroy()

        self.frame = Frame(self.master, bg='green', bd=5)
        self.frame.grid(column=0, row=9, columnspan=6)

        label1 = Label(self.frame, text='Dark power')
        label1.grid(column=0, row=0, sticky=W + E + N + S)
        label2 = Label(self.frame, text='Padavan')
        label2.grid(column=2, row=0, sticky=W + E + N + S)

        self.scale = Scale(self.frame,
                           orient=HORIZONTAL,
                           length=500,
                           from_=-50, to=50,
                           tickinterval=10,
                           resolution=5)
        self.scale.grid(column=1, row=0)

    def black_and_whiteAction(self):
        self.frame.destroy()

        self.frame = Frame(self.master, bg='green', bd=5)
        self.frame.grid(column=0, row=9, columnspan=6)

        label1 = Label(self.frame, text='East coast')
        label1.grid(column=0, row=0, sticky=W + E + N + S)
        label2 = Label(self.frame, text='West coast')
        label2.grid(column=2, row=0, sticky=W + E + N + S)

        self.scale = Scale(self.frame,
                           orient=HORIZONTAL,
                           length=500,
                           from_=-150, to=150,
                           tickinterval=10,
                           resolution=5)
        self.scale.grid(column=1, row=0)

    def noiseAction(self):
        self.frame.destroy()

        self.frame = Frame(self.master, bg='green', bd=5)
        self.frame.grid(column=0, row=9, columnspan=6)

        label1 = Label(self.frame, text='Wonderfull day')
        label1.grid(column=0, row=0, sticky=W + E + N + S)
        label2 = Label(self.frame, text='Slenderman')
        label2.grid(column=2, row=0, sticky=W + E + N + S)

        self.scale = Scale(self.frame,
                           orient=HORIZONTAL,
                           length=500,
                           from_=0, to=100,
                           tickinterval=10,
                           resolution=5)
        self.scale.grid(column=1, row=0)

    def customAction(self):
        self.frame.destroy()

        self.frame = Frame(self.master, bg='green', bd=5)
        self.frame.grid(column=0, row=9, columnspan=6)

        label1 = Label(self.frame, text='Low concentration')
        label1.grid(column=0, row=0, sticky=W + E + N + S)
        label2 = Label(self.frame, text='High concentration')
        label2.grid(column=5, row=0, sticky=W + E + N + S)

        self.scale = Scale(self.frame,
                           orient=HORIZONTAL,
                           length=500,
                           from_=0, to=100,
                           tickinterval=10,
                           resolution=5)
        self.scale.grid(column=1, row=0, columnspan=4)

        label3 = Label(self.frame, text='R')
        label3.grid(column=0, row=1, sticky=W + E + N + S)
        label4 = Label(self.frame, text='G')
        label4.grid(column=2, row=1, sticky=W + E + N + S)
        label5 = Label(self.frame, text='B')
        label5.grid(column=4, row=1, sticky=W + E + N + S)

        self.entry_r = Entry(self.frame)
        self.entry_r.grid(column=1, row=1, sticky=W + E + N + S)
        self.entry_g = Entry(self.frame)
        self.entry_g.grid(column=3, row=1, sticky=W + E + N + S)
        self.entry_b = Entry(self.frame)
        self.entry_b.grid(column=5, row=1, sticky=W + E + N + S)

    def add_file(self):
        text = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"),
                                                     ("bmp files", "*.bmp"),
                                                     ("png files", "*.png")
                                                     # ("all files", "*.*")
                                                     ))
        self.listbox.insert(END, text)

    def del_file(self):
        select = list(self.listbox.curselection())
        select.reverse()
        for i in select:
            self.listbox.delete(i)

    def try_file(self):

        try:
            select = self.listbox.get(0, self.listbox.curselection())
        except:
            self.str_info.set('Select a picture, please.')
        else:
            select = self.resize_image(input_image_path=select[0], size=(280, 280))
            value = self.var.get()
            image = Image.open(select)
            try:
                draw = ImageDraw.Draw(image)
                photo_original = ImageTk.PhotoImage(image)
            except:
                self.str_info.set('Error, file a not work')
            else:
                self.original_photo.image = photo_original  # <--- keep reference of your image
                self.original_photo.create_image(0, 0, anchor='nw', image=photo_original)
                pix = image.load()

                if value == 0:
                    self.str_info.set('Please chose a filter')
                elif value == 1:
                    path_file = F.negative(image=image, draw=draw, pix=pix)
                    del draw

                    image = Image.open(path_file)
                    photo_edit = ImageTk.PhotoImage(image)

                    self.edit_photo.image = photo_edit  # <--- keep reference of your image
                    self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)

                    remove(path_file)

                elif value == 2:
                    path_file = F.gray(image=image, draw=draw, pix=pix)
                    del draw

                    image = Image.open(path_file)
                    photo_edit = ImageTk.PhotoImage(image)

                    self.edit_photo.image = photo_edit  # <--- keep reference of your image
                    self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)

                    remove(path_file)

                elif value == 3:
                    path_file = F.sepia(image=image, draw=draw, pix=pix, depth=self.scale.get())
                    del draw

                    image = Image.open(path_file)
                    photo_edit = ImageTk.PhotoImage(image)

                    self.edit_photo.image = photo_edit  # <--- keep reference of your image
                    self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)

                    remove(path_file)

                elif value == 4:
                    path_file = F.bright(image=image, draw=draw, pix=pix, factor=self.scale.get())
                    del draw

                    image = Image.open(path_file)
                    photo_edit = ImageTk.PhotoImage(image)

                    self.edit_photo.image = photo_edit  # <--- keep reference of your image
                    self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)

                    remove(path_file)

                elif value == 5:
                    path_file = F.contrast(image=image, draw=draw, pix=pix, coefficient=self.scale.get())
                    del draw

                    image = Image.open(path_file)
                    photo_edit = ImageTk.PhotoImage(image)

                    self.edit_photo.image = photo_edit  # <--- keep reference of your image
                    self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)

                    remove(path_file)

                elif value == 6:
                    path_file = F.black_white(image=image, draw=draw, pix=pix, factor=self.scale.get())
                    del draw

                    image = Image.open(path_file)
                    photo_edit = ImageTk.PhotoImage(image)

                    self.edit_photo.image = photo_edit  # <--- keep reference of your image
                    self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)

                    remove(path_file)

                elif value == 7:
                    path_file = F.noise(image=image, draw=draw, pix=pix, factor=self.scale.get())
                    del draw

                    image = Image.open(path_file)
                    photo_edit = ImageTk.PhotoImage(image)

                    self.edit_photo.image = photo_edit  # <--- keep reference of your image
                    self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)

                    remove(path_file)

                elif value == 8:
                    try:
                        r = int(self.entry_r.get())
                        g = int(self.entry_g.get())
                        b = int(self.entry_b.get())

                    except ValueError:
                        r, g, b = 0, 0, 0
                    finally:

                        path_file = F.custom(image=image, draw=draw, pix=pix, depth=self.scale.get(),
                                             r_custom=r,
                                             g_custom=g,
                                             b_custom=b)
                        del draw
                        image = Image.open(path_file)
                        photo_edit = ImageTk.PhotoImage(image)

                        self.edit_photo.image = photo_edit  # <--- keep reference of your image
                        self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)
                        remove(path_file)

            finally:
                remove(select)

    def save_photo(self):

        try:
            select = self.listbox.get(0, self.listbox.curselection())
        except:
            self.str_info.set('Select a picture, please.')
        else:
            select = select[0]
            value = self.var.get()
            image = Image.open(select)
            try:
                draw = ImageDraw.Draw(image)
            except:
                self.str_info.set('Error, file a not work')
            else:
                pix = image.load()

                if value == 0:
                    self.str_info.set('Please chose a filter')

                elif value == 1:
                    F.negative(image=image, draw=draw, pix=pix, file_extension=self.extension)
                    del draw

                elif value == 2:
                    F.gray(image=image, draw=draw, pix=pix, file_extension=self.extension)
                    del draw

                elif value == 3:
                    F.sepia(image=image, draw=draw, pix=pix, depth=self.scale.get(), file_extension=self.extension)
                    del draw

                elif value == 4:
                    F.bright(image=image, draw=draw, pix=pix, factor=self.scale.get(), file_extension=self.extension)
                    del draw

                elif value == 5:
                    F.contrast(image=image, draw=draw, pix=pix, coefficient=self.scale.get(), file_extension=self.extension)
                    del draw

                elif value == 6:
                    F.black_white(image=image, draw=draw, pix=pix, factor=self.scale.get(), file_extension=self.extension)
                    del draw

                elif value == 7:
                    F.noise(image=image, draw=draw, pix=pix, factor=self.scale.get(), file_extension=self.extension)
                    del draw

                elif value == 8:
                    try:
                        r = int(self.entry_r.get())
                        g = int(self.entry_g.get())
                        b = int(self.entry_b.get())

                    except ValueError:
                        r, g, b = 0, 0, 0
                    finally:

                        F.custom(image=image, draw=draw, pix=pix, depth=self.scale.get(),
                                 r_custom=r,
                                 g_custom=g,
                                 b_custom=b,
                                 file_extension=self.extension)
                        del draw

        finally:
            self.str_info.set('Your photo is saved in a folder /Resources')

    def resize_image(self, input_image_path, size):
        time_save = datetime.today().timetuple()
        output_image_path = "Resources/Temp/_{}{}{}_{}{}{}{}.jpg".format(
            time_save[0],
            time_save[1],
            time_save[2],
            time_save[3],
            time_save[4],
            time_save[5],
            time_save[6])

        original_image = Image.open(input_image_path)

        resized_image = original_image.resize(size)

        resized_image.save(output_image_path)
        return output_image_path

    def __del__(self):
        remove(self.path_image)


apply_window = Tk()

AppObj = MainClass(apply_window)

apply_window.mainloop()
