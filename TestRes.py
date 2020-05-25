from PIL import Image
from datetime import datetime


def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    # width, height = original_image.size
    # print('The original image size is {wide} wide x {height} '
    #       'high'.format(wide=width, height=height))
    resized_image = original_image.resize(size)
    # width, height = resized_image.size
    # print('The resized image size is {wide} wide x {height} '
    #       'high'.format(wide=width, height=height))
    # #resized_image.show()
    resized_image.save(output_image_path)


time_save = datetime.today().timetuple()
resize_image(input_image_path='Examples/3.jpg',
             output_image_path="Resources/Temp/_{}{}{}_{}{}{}{}.jpg".format(
                 time_save[0],
                 time_save[1],
                 time_save[2],
                 time_save[3],
                 time_save[4],
                 time_save[5],
                 time_save[6]),
             size=(200, 200))
