import random
from datetime import datetime


def save(image, name_filter, file_extension='jpg'):
    time_save = datetime.today().timetuple()

    try:
        output_image_path = "Resources/{}{}{}_{}{}{}{}({}).{}".format(
            time_save[0],
            time_save[1],
            time_save[2],
            time_save[3],
            time_save[4],
            time_save[5],
            time_save[6],
            name_filter,
            file_extension)
        image.save(output_image_path)
    except:
        print("Error, file cannot be saved.")
    else:
        print("Saved successfully.")
        return output_image_path


def negative(image, draw, pix, file_extension='jpg'):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pix[i, j]
            draw.point((i, j), (255 - r, 255 - g, 255 - b))
    del draw
    return save(image, 'negative', file_extension)


def gray(image, draw, pix, file_extension='jpg'):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pix[i, j]

            avg = (r + g + b) // 3

            draw.point((i, j), (avg, avg, avg))
    del draw
    return save(image, 'gray', file_extension)


# 0 < and >100 ??
def sepia(image, draw, pix, depth, file_extension='jpg'):
    # depth = int(input('depth:'))

    for i in range(image.size[0]):
        for j in range(image.size[1]):

            r, g, b = pix[i, j]

            avg = (r + g + b) // 3

            r = avg + depth * 2
            g = avg + depth
            b = avg

            if r > 255: r = 255
            if g > 255: g = 255
            if b > 255: b = 255

            draw.point((i, j), (r, g, b))
    del draw
    return save(image, 'sepia', file_extension)


# < 0 and > 100
def bright(image, draw, pix, factor, file_extension='jpg'):
    # factor = int(input('factor:'))

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r = factor + pix[i, j][0]
            g = factor + pix[i, j][1]
            b = factor + pix[i, j][2]

            if r < 0: r = 0
            if g < 0: g = 0
            if b < 0: b = 0

            if r > 255: r = 255
            if g > 255: g = 255
            if b > 255: b = 255

            draw.point((i, j), (r, g, b))
    del draw
    return save(image, 'bright', file_extension)


# < -50 and >50
def contrast(image, draw, pix, coefficient, file_extension='jpg'):
    # coefficient = int(input("coefficient: ")) / 2

    avg = 0

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pix[i, j]

            avg += (r * 0.299 + g * 0.587 + b * 0.114)

    avg /= image.size[0] * image.size[1]

    palette = []
    for i in range(256):

        temp = int(avg + coefficient * (i - avg))

        if temp < 0: temp = 0
        if temp > 255: temp = 255

        palette.append(temp)

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pix[i, j]

            draw.point((i, j), (palette[r], palette[g], palette[b]))

    del draw
    return save(image, 'contrast', file_extension)


# < -150 and >150
def black_white(image, draw, pix, factor, file_extension='jpg'):
    # factor = int(input('factor:'))

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pix[i, j]

            avg = r + g + b

            if avg > (((255 + factor) // 2) * 3):
                r, g, b = 255, 255, 255
            else:
                r, g, b = 0, 0, 0
            draw.point((i, j), (r, g, b))
    del draw
    return save(image, 'black_white',file_extension)


# < 0 and > 1000
def noise(image, draw, pix, factor, file_extension='jpg'):
    # factor = int(input('factor:'))

    for i in range(image.size[0]):
        for j in range(image.size[1]):

            rand = random.randint(-factor, factor)

            r = pix[i, j][0] + rand
            g = pix[i, j][1] + rand
            b = pix[i, j][2] + rand

            if r < 0: r = 0
            if g < 0: g = 0
            if b < 0: b = 0

            if r > 255: r = 255
            if g > 255: g = 255
            if b > 255: b = 255
            draw.point((i, j), (r, g, b))
    del draw
    return save(image, 'noise', file_extension)


def custom(image, draw, pix, depth, r_custom, g_custom, b_custom, file_extension='jpg'):

    for i in range(image.size[0]):
        for j in range(image.size[1]):

            r, g, b = pix[i, j]

            r += r_custom + depth
            g += g_custom + depth
            b += b_custom + depth

            if r > 255: r = 255
            if g > 255: g = 255
            if b > 255: b = 255

            draw.point((i, j), (r, g, b))
    del draw
    return save(image, 'custom', file_extension)

