from datetime import datetime, date, time
from tkinter import *
from os import path
from PIL import Image, ImageDraw

class Applying(object):
    apply_window = Tk()
    apply_window.title("Select a filter for each photo.")
    apply_window.geometry('800x600')  # '800x600'

    #def negativ_BtnAction():

    def save(self, image, filter_name):
        full_name = path.basename(self.getImage_path())
        name = path.splitext(full_name)[0]

        time_save = datetime.today().timetuple()

        try:
            image.save(
                "Resources//({}){}_{}{}{}_{}{}{}{}.{}".format(
                    name,
                    filter_name,
                    time_save[0],
                    time_save[1],
                    time_save[2],
                    time_save[3],
                    time_save[4],
                    time_save[5],
                    time_save[6],
                    self.getFile_extension()))
        except:
            print("Error, file cannot save.")
        else:
            print("Saved successfully.")
        finally:
            del self.draw

    def getImage_path(self):
        return self.image_path

    def setImage_path(self, image_path):
        self.image_path = image_path

    def getFile_extension(self):
        return self.file_extension

    def setFile_extension(self, file_extension):
        self.file_extension = file_extension

    image_path = 'Examples/2.jpg'
    file_extension = 'png'  # jpg jpeg bmp png

    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    pix = image.load()



# Negative.
btn_neg = Button(apply_window, text="Custom", command=custom(image, draw, pix))
btn_neg.grid(column=1, row=0, sticky=W + E + N + S)
# Grayscale.
# btn_gray = Button(apply_window, text="Add a file", command=gray)
# btn_gray.grid(column=1, row=0, sticky=W + E + N + S)
# # Sepia.
# btn_sepia = Button(apply_window, text="Add a file", command=sepia)
# btn_sepia.grid(column=1, row=0, sticky=W + E + N + S)
# Brightness changes.
# btn_bright = Button(apply_window, text="Add a file", command=add_file)
# btn_bright.grid(column=1, row=0, sticky=W + E + N + S)
# # Contrast.
# btn_contrast = Button(apply_window, text="Add a file", command=add_file)
# btn_contrast.grid(column=1, row=0, sticky=W + E + N + S)
# # Black and white.
# btn_Black_White = Button(apply_window, text="Add a file", command=add_file)
# btn_Black_White.grid(column=1, row=0, sticky=W + E + N + S)
# # Adding noise.
# btn_noise = Button(apply_window, text="Add a file", command=add_file)
# btn_noise.grid(column=1, row=0, sticky=W + E + N + S)

apply_window.mainloop()
