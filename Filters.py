import random


class Filtters(object):
    def negative(self, image, draw, pix):
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r, g, b = pix[i, j]

                draw.point((i, j), (255 - r, 255 - g, 255 - b))

    def gray(self, image, draw, pix):
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r, g, b = pix[i, j]

                avg = (r + g + b) // 3

                draw.point((i, j), (avg, avg, avg))

    # 0 < and >100 ??
    def sepia(self, image, draw, pix):
        depth = int(input('depth:'))

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
        # image.save("Resources/ans.jpg", "JPEG")
        # del draw

    # < 0 and > 100
    def bright(self, image, draw, pix):
        factor = int(input('factor:'))

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
        # image.save("Resources/ans.jpg", "JPEG")
        # del draw

    # < -50 and >50
    def contrast(self, image, draw, pix):
        coefficient = int(input("coefficient: ")) / 2

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

        # image.save("Resources/ans.jpg", "JPEG")
        # del draw

    # < -150 and >150
    def black_white(self, image, draw, pix):
        factor = int(input('factor:'))

        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r, g, b = pix[i, j]

                avg = r + g + b

                if avg > (((255 + factor) // 2) * 3):
                    r, g, b = 255, 255, 255
                else:
                    r, g, b = 0, 0, 0
                draw.point((i, j), (r, g, b))
        # image.save("Resources/ans.jpg", "JPEG")
        # del draw

    # < 0 and > 1000
    def noise(self, image, draw, pix):
        factor = int(input('factor:'))

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
        # image.save("Resources/ans.jpg", "JPEG")
        # del draw

    def custom(self, image, draw, pix):
        depth = int(input('depth:'))

        r1 = int(input("R: "))
        g1 = int(input("G: "))
        b1 = int(input("B: "))

        for i in range(image.size[0]):
            for j in range(image.size[1]):

                r, g, b = pix[i, j]

                r += r1 + depth
                g += g1 + depth
                b += b1 + depth

                if r > 255: r = 255
                if g > 255: g = 255
                if b > 255: b = 255

                draw.point((i, j), (r, g, b))
