__author__ = 'bene'

class PyFcFonts:
    font2Line = {
        "meta":{"height": 5, "width":3},

        "1":"""
#*#
**#
#*#
#*#
***""",
        "2":"""
***
##*
***
*##
***""",
        "3":"""
***
##*
***
##*
***""",
        "4":"""
*#*
*#*
***
##*
##*""",
        "5":"""
***
*##
***
##*
***""",
        "6":"""
***
*##
***
*#*
***""",
        "7":"""
***
##*
#*#
#*#
#*#""",
        "8":"""
***
*#*
***
*#*
***""",
        "9":"""
***
*#*
***
##*
***""",
        "0":"""
***
*#*
*#*
*#*
***""",
        ":":"""
###
#*#
###
#*#
###""",}

    aktFont = font2Line

    def __init__(self, font):
        self.aktFont = font;

    def __init__(self):
        pass

    def drawText(self, frame, x,y, text):
        self.drawText(frame, x,y, text, 0xff, 0xff, 0xff)

    def drawText(self, frame, x,y, text, r,g,b):

        origX = x
        origY = y

        for char in text:

            if char == "\n":
                y += self.aktFont["meta"]["height"] + 1
                x = origX
                continue

            if not self.aktFont[char]:
                char = char.upper()

            if not self.aktFont[char]:
                continue

            c = self.aktFont[char].strip()
            cx=0
            cy=0
            for line in c:
                if line == "*":
                    frame.setColorForPixel (x + cx, y + cy, r, g, b)
                if line == "\n":
                    cx = 0
                    cy += 1
                    continue
                cx += 1

            x += self.aktFont["meta"]["width"] + 1

    def getPixelForChar(self, char):

        c = self.aktFont[char].strip()
        #  c = char.split("\n")
        ret = []

        y = 0
        x = 0

        for line in c:
            if line == "*":
                ret.append([x,y])
            if line == "\n":
                x=-1
                y+=1
            x+=1

        return ret