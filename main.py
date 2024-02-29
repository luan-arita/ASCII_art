from PIL import Image
import numpy  as np
import pyperclip
from colorama import Fore, Style

ASCII_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

MAX_RGB_VALUE = 255

#gets the arrays of rgb from all the pixels of the image. Includes the im.thumbnail function where we can set how big we want our converted image to be through the "height" variable.
def get_rgb_array(im, height):
    im.thumbnail((height, 1000))
    print(im.size)
    return np.array(im)

#transforms the array into basically a list of lists, to make things easier to work with
def get_rgb_matrix(pixel_array):
    rgb_matrix = []
    for row in pixel_array:
        intensity_row = []
        for column in row:
            intensity_row.append(column)
        rgb_matrix.append(intensity_row)
    return rgb_matrix

#column[0] = R, column[1] = G, column[2] = B, which form the three values from RGB matrix
#converts the three values from RGB data into single brightness numbers, using three different ways of conversion, those being the average, lightness and luminosity accounted for human perception. Some images may end up looking better by changing this.
def get_brightness_matrix(rgb_matrix, algo_name = 'average'):
    brightness_matrix = []
    for row in rgb_matrix:
        brightness_row = []
        for column in row:
            if algo_name == 'average':
                brightness = ((column[0] + column[1] + column[2]) / 3.0)
            elif algo_name == 'lightness':
                brightness = ((max(column) + min(column)) / 2.0)
            elif algo_name == 'luminosity':
                brightness = (column[0]*0.21 + column[1]*0.72 + column[2]*0.07)
            brightness_row.append(brightness)
        brightness_matrix.append(brightness_row)
    return brightness_matrix

def get_inverted_brightness_matrix(brightness_matrix):
    inverted_brightness_matrix = []
    for row in brightness_matrix:
        inverted_row = []
        for column in row:
            inverted_row.append(MAX_RGB_VALUE - column)
        inverted_brightness_matrix.append(inverted_row)
    return inverted_brightness_matrix

#converts the single brightness numbers into its respective ASCII char. returns a list containing all the ASCII characters, which then we just need to print to visualize it.
def get_ASCII_matrix(brightness_matrix, ascii_chars):
    brightness_interval = MAX_RGB_VALUE / len(ASCII_chars)
    output = []
    for row in brightness_matrix:
        row_ascii_art = []
        for column in row:
            index = int(column/brightness_interval) - 1
            if index == -1:
                index = 0
            row_ascii_art.append(ascii_chars[index] *2)
        output.append(row_ascii_art)
    return output

def getreducedcolor_matrix(rgb_matrix):
    reducedColor = []
    for row in rgb_matrix:
        row_reducedColor = []
        for column in row:
            i = column[0] >> 7
            j = column[1] >> 7
            k = column[2] >> 7
            row_reducedColor.append(str(i)+str(j)+str(k))
        reducedColor.append(row_reducedColor)
    return reducedColor

def getReducedPixelColor(s):
    if s == "000":
        return Fore.BLACK
    elif s == "100":
        return Fore.RED
    elif s == "010":
        return Fore.GREEN
    elif s == "001":
        return Fore.BLUE
    elif s == "110":
        return Fore.YELLOW
    elif s == "011":
        return Fore.CYAN
    elif s == "101":
        return Fore.MAGENTA
    else:
        return Fore.WHITE

def print_ascii_matrix(ascii_matrix, reducedcolor_matrix):
    for i, row in enumerate(ascii_matrix):
        for j, p in enumerate(row):
            color = getReducedPixelColor(reducedcolor_matrix[i][j])
            print(color + p, end = "")
        print("")
    return(Style.RESET_ALL)

im = Image.open("C:/Users/Luan\Desktop/faculdade/Python/ASCII/julha.jpg")


pixel_array = get_rgb_array(im, 300)
#print(get_brightness_matrix(pixel_array))
rgb_matrix = get_rgb_matrix(pixel_array)
brightness_matrix = get_brightness_matrix(rgb_matrix, 'average')
inverted_brightness_matrix = get_inverted_brightness_matrix(brightness_matrix)
#ascii_matrix = get_ASCII_matrix(brightness_matrix, ASCII_chars)
ascii_matrix = get_ASCII_matrix(inverted_brightness_matrix, ASCII_chars)
reducedcolor_matrix = getreducedcolor_matrix(rgb_matrix)
print_ascii_matrix(ascii_matrix, reducedcolor_matrix)

#print(reducedcolor_matrix)
#print(ascii_matrix)
