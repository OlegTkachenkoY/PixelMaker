from datetime import datetime
from tkinter import *
from os import remove
from PIL import Image, ImageDraw, ImageTk
from tkinter import filedialog
import Filters as F


class MainClass:
    def __init__(self, master):
        """
        Objects for the interface are created in the designer, and also variables are declared.
        To instantiate a class, you must pass the main window to the class
        """

        # The passed variable is assigned to the created variable in the class
        self.master = master

        # Project title.The size of the main window
        self.master.title("PixelMaker")
        self.master.geometry('1200x400')

        # The path to the example is passed to the function where the photo is compressed
        self.path_image = self.resize_image(
            input_image_path="Examples/3.jpg",  #The path to the example
            size=(280, 280))                    #size

        #Opening and saving a photo as a variable
        image = Image.open(self.path_image)
        photo = ImageTk.PhotoImage(image)

        #Creating a container for widgets
        self.frame = Frame(self.master)

        #A list is created in which we will add the path to the file, and place it in the window with grid
        self.listbox = Listbox(self.master)
        self.listbox.grid(column=0, row=0, rowspan=7, sticky=W + E + N + S, ipadx=50, ipady=40)

        #Creating a variable to transmit information to the user, set the start data
        self.str_info = StringVar()
        self.str_info.set('Hello, this is info label. I help you.\n At start chose you photo. (Add a file)')

        #Creating a window to information, set position in Frame
        self.label_info = Label(self.master,
                                textvariable=self.str_info,
                                bg='green')
        self.label_info.grid(column=0, row=7, sticky=W + E + N + S)

        #Creating a canvas for an example of the original photo,
        # Inserting the photo into the canvas,
        # placing in a frame.
        self.original_photo = Canvas(self.master, height=280, width=280)
        self.original_photo.image = photo  # <--- keep reference of your image
        self.original_photo.create_image(0, 0, anchor='nw', image=photo)
        self.original_photo.grid(column=2, row=0, rowspan=9)

        # Creating a canvas for an example of the editable photo,
        # Inserting the photo into the canvas,
        # placing in a frame.
        self.edit_photo = Canvas(self.master, height=280, width=280)
        self.edit_photo.image = photo  # <--- keep reference of your image
        self.edit_photo.create_image(0, 0, anchor='nw', image=photo)
        self.edit_photo.grid(column=4, row=0, rowspan=9)

        #Variable for radiobuttons, it is needed to read which button is pressed
        self.var = IntVar()

        #Creation of 8 buttons for filters, all buttons are almost identical,
        #only the location in the main window changes, and the command.
        #(Therefore, I will describe only one button)
        self.rbutton1 = Radiobutton(self.master,                    #Button location
                                    text='Negative',                #Button name
                                    variable=self.var,              #variable that changes when pressed
                                    indicatoron=0,                  #Button view
                                    value=1,                        #the value assigned to the variable
                                    command=self.negativ_grayAction)#The command used when pressing
        self.rbutton1.grid(column=3, row=0,         #Button location
                           sticky=W + E + N + S)    #Stretching the button on all sides

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

        #The main buttons for actions in the program.
        #Add - adds a file
        #Delete - deletes the selected file
        #Try - make a small copy of the photo and try the filters
        #Save - saves the photo
        #(the buttons are almost the same so I will describe only one)
        btn_add = Button(self.master,                   #Button location
                         text="Add a file",             #Button name
                         command=self.add_file)         #The command used when pressing
        btn_add.grid(column=1, row=0,                   #Button location
                     rowspan=4,                         #Stretch the button in several rows
                     sticky=W + E + N + S)              #Stretching the button on all sides
        btn_del = Button(self.master, text="Delete the file", command=self.del_file)
        btn_del.grid(column=1, row=4, rowspan=4, sticky=W + E + N + S)
        btn_try = Button(self.master, text="Look at the photo", command=self.try_file)
        btn_try.grid(column=5, row=0, rowspan=4, sticky=W + E + N + S)
        btn_save = Button(self.master, text="Save", command=self.save_photo)
        btn_save.grid(column=5, row=4, rowspan=4, sticky=W + E + N + S)

        #Default photo format
        self.extension = 'jpg'

        #Buttons for selecting the file format (default .jpg)
        # (the buttons are almost the same so I will describe only one)
        btn_jpeg = Button(self.master,                  #Button location
                          text=".jpeg",                 #Button name
                          command=self.jpegAction)      #The command used when pressing
        btn_jpeg.grid(column=6, row=4,                  #Button location
                      sticky=W + E + N + S)             #Stretching the button on all sides
        btn_jpg = Button(self.master, text=".jpg", command=self.jpgAction)
        btn_jpg.grid(column=6, row=5, sticky=W + E + N + S)
        btn_bmp = Button(self.master, text=".bmp", command=self.bmpAction)
        btn_bmp.grid(column=6, row=6, sticky=W + E + N + S)
        btn_png = Button(self.master, text=".png", command=self.pngAction)
        btn_png.grid(column=6, row=7, sticky=W + E + N + S)

    def jpegAction(self):
        """
        Called when the button is pressed jpeg changes the variable extension to jpeg
        """
        self.extension = 'jpeg'                                         #data change
        self.str_info.set('Your photo will be saved in .jpeg format')   #ichange info in Label

    def jpgAction(self):
        """
        Called when the button is pressed jpg changes the variable extension to jpg
        """
        self.extension = 'jpg'                                          #data change
        self.str_info.set('Your photo will be saved in .jpg format')    #ichange info in Label

    def bmpAction(self):
        """
        Called when the button is pressed bmp changes the variable extension to bmp
        """
        self.extension = 'bmp'                                          #data change
        self.str_info.set('Your photo will be saved in .bmp format')    #ichange info in Label

    def pngAction(self):
        """
        Called when the button is pressed png changes the variable extension to png
        """
        self.extension = 'png'                                          #data change
        self.str_info.set('Your photo will be saved in .png format')    #ichange info in Label


    def negativ_grayAction(self):
        """
        Starts when the Negativ button is pressed. Makes a change in the Frame container
        """
        self.frame.destroy()        #Del frame

    def sepiaAction(self):
        """
        Starts when the Sepia button is pressed. Makes a change in the Frame container
        """
        self.frame.destroy()  # Del frame

        #Basically all filter buttons are the same so I write only one function for example
        self.frame = Frame(self.master,         #Location
                           bg='green',          #background
                           bd=5)                #borderwidth
        self.frame.grid(column=0, row=9,        #Coordinates in the grid
                        columnspan=7)           #expanded to 7 columns

        #Ordinary captions are created, without the word self,
        # because in the future they do not need to be edited,
        # they exist only in the function
        label1 = Label(self.frame, text='new')
        label1.grid(column=0, row=0, sticky=W + E + N + S)
        label2 = Label(self.frame, text='60s')
        label2.grid(column=2, row=0, sticky=W + E + N + S)

        #scale to select concentration, filter (Also to select contrast)
        self.scale = Scale(self.frame,          #Location(Not in Master!!!)
                           orient=HORIZONTAL,   #Horizontally located
                           length=500,
                           from_=0, to=100,
                           tickinterval=10,     #The interval between numbers
                           resolution=5)
        self.scale.grid(column=1, row=0)

    def brightAction(self):
        """
        Starts when the bright button is pressed. Makes a change in the Frame container
        """
        self.frame.destroy()  # Del frame

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
        """
        Starts when the contrast button is pressed. Makes a change in the Frame container
        """
        self.frame.destroy()  # Del frame

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
        """
        Starts when the Black and White button is pressed. Makes a change in the Frame container
        """
        self.frame.destroy()  # Del frame

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
        """
        Starts when the noise button is pressed. Makes a change in the Frame container
        """
        self.frame.destroy()  # Del frame

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
        """
        Starts when the custom button is pressed. Makes a change in the Frame container
        """
        self.frame.destroy()  # Del frame

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

        #Created regular fields for entering colors in the format RGB
        self.entry_r = Entry(self.frame)
        self.entry_r.grid(column=1, row=1, sticky=W + E + N + S)
        self.entry_g = Entry(self.frame)
        self.entry_g.grid(column=3, row=1, sticky=W + E + N + S)
        self.entry_b = Entry(self.frame)
        self.entry_b.grid(column=5, row=1, sticky=W + E + N + S)


    def add_file(self):
        """
        The function allows you to select a file, it is fixed with the element filedialog.askopenfilename.
        The result is recorded in listbox
        """

        text = filedialog.askopenfilename(initialdir="/",                       #Starting position
                                          title="Select file",                  #Name
                                          filetypes=(("jpeg files", "*.jpg"),   #File formats
                                                     ("bmp files", "*.bmp"),
                                                     ("png files", "*.png")
                                                     # ("all files", "*.*")
                                                     ))
        self.listbox.insert(END, text)

    def del_file(self):
        """
        The function is activated by pressing the Del button,
        after which the selected file is deleted.
        """
        select = list(self.listbox.curselection())      #the selected file is written to the variable, if any

        #The loop is needed to delete a number of selected files.
        for i in select:
            self.listbox.delete(i)                      #Del

    def try_file(self):
        """
        This feature creates a small copy of the selected photo and uses the selected filter on it.
        The procedure for applying the filter is quite complicated,
        so in order for the user to be able to view their photo, I decided to do this feature.
        Its main goal is to reduce the waiting time for the user.
        As a result, the photo and the edited photo are saved in the canvas for viewing.
        """
        #The first block checks for an error, it occurs if the user does not select a file
        try:
            select = self.listbox.get(0, self.listbox.curselection())
        except:     #_tkinter.TclError
            # select = 'Examples/3.jpg'
            self.str_info.set('Select a picture, please.') #If an error occurs, the user immediately sees it
        else:
            #Filter value
            value = self.var.get()
            # transfer a photo to compress it
            select = self.resize_image(input_image_path=select[0], size=(280, 280))
            # Writes a photo to the object
            image = Image.open(select)

            #Checks if the file can be opened
            try:

                #Writes the object as a picture
                draw = ImageDraw.Draw(image)
                #open the object
                photo_original = ImageTk.PhotoImage(image)
            except: #PIL.UnidentifiedImageError
                self.str_info.set('Error, file a not work') #If an error occurs, the user immediately sees it
            else:
                #Fills a photo without a filter in the left canvas
                self.original_photo.image = photo_original  # <--- keep reference of image
                self.original_photo.create_image(0, 0, anchor='nw', image=photo_original)
                #Loads pixels
                pix = image.load()

                if value == 0:
                    #If the user does not select a filter, he will know about it immediately
                    self.str_info.set('Please chose a filter')
                elif value == 1:
                    #The following blocks are about the same so I will describe only this one
                    #sends the compressed photo to the filter and returns the path of the new one
                    path_file = F.negative(image=image, draw=draw, pix=pix)

                    del draw    #del draw

                    #Opens a photo and writes to a variable
                    image = Image.open(path_file)
                    photo_edit = ImageTk.PhotoImage(image)

                    #Replaces the photo on the left canvas
                    self.edit_photo.image = photo_edit  # <--- keep reference of your image
                    self.edit_photo.create_image(0, 0, anchor='nw', image=photo_edit)

                    #Deletes the created file
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
        """Function for saving photos, input: Path, idi filter. As a result, saves the photo"""
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
        """
        resizes the photo, unfortunately in some cases it compresses the photo incorrectly
        (when the photo does not look like a square, and the entered sizes are as for a square)
        Ideally, you still need to create a mechanism that assigns the ratio of the parties and reduces them,
        but unfortunately I have not figured out how to do it
        input:
            way photo
            size
        output:
            compressed photo path
        """

        #saves file compression time
        time_save = datetime.today().timetuple()

        #Creates a new way to save a photo
        output_image_path = "Resources/Temp/_{}{}{}_{}{}{}{}.jpg".format(
            time_save[0],
            time_save[1],
            time_save[2],
            time_save[3],
            time_save[4],
            time_save[5],
            time_save[6])

        #Opens a photo
        original_image = Image.open(input_image_path)

        #Compressed
        resized_image = original_image.resize(size)

        #Saves
        resized_image.save(output_image_path)
        #returns the path of the edited photo

        return output_image_path

    def __del__(self):
        """Deletes objects after class execution"""
        #Deletes the sample photo
        remove(self.path_image)

#######START########

apply_window = Tk()

AppObj = MainClass(apply_window)

apply_window.mainloop()
