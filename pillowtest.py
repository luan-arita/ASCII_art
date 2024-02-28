from PIL import Image
import numpy  as np
import pyperclip
from colorama import Fore, Style

ASCII_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

MAX_RGB_VALUE = 255

def get_rgb_array(im, height):
    im.thumbnail((height, 350))
    print(im.size)
    return np.array(im)

def round_average(number):
    average = number / 3
    return round(average)

def get_rgb_matrix(pixel_array):
    rgb_matrix = []
    for row in pixel_array:
        intensity_row = []
        for column in row:
            sum = np.sum(column)
            intensity_row.append(round_average(sum))
        rgb_matrix.append(intensity_row)
    return rgb_matrix

#get_ASCII_matrix returns a list, where each row represents a list inside the list. Therefore, you need a separate print function in order to view the output
def get_ASCII_matrix(brightness_matrix, ascii_chars):
    brightness_interval = MAX_RGB_VALUE / len(ASCII_chars)
    output = []
    for row in brightness_matrix:
        row_ascii_art = []
        for column in row:
            index = int(column/brightness_interval) - 1
            row_ascii_art.append(ascii_chars[index] *2)
        output.append(row_ascii_art)
    return output

def print_ascii_matrix(ascii_matrix, text_color):
    for row in ascii_matrix:
        line = [p for p in row]
        print(text_color + "".join(line))
    
    return(Style.RESET_ALL)

im = Image.open("C:/Users/Luan\Desktop/faculdade/Python/ASCII/640x480.jpg")


pixel_array = get_rgb_array(im, 2000)
#print(get_brightness_matrix(pixel_array))
matrix = get_rgb_matrix(pixel_array)
ascii_matrix = get_ASCII_matrix(matrix, ASCII_chars)
#pyperclip.copy(get_ASCII_matrix(matrix, ASCII_chars))
#print(get_ASCII_matrix(matrix, ASCII_chars))
print_ascii_matrix(ascii_matrix, Fore.GREEN)



