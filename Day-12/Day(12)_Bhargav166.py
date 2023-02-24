# - Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
# - Write a function generate_colors which can generate any number of hexa or rgb colors.

import random


def list_of_hexa_colors(n):
    hex_colors = []
    for i in range(n):
        colors = '#'
        for i in range(6):
            colors += random.choice('0123456789abcdefg')
        hex_colors.append(colors)
    return hex_colors


def list_of_rgb_colors(n):
    rgb_colors = []
    for i in range(n):
        colors = 'rgb('
        for i in range(3):
            colors += str(random.randint(0, 255)) + ','
        colors = colors[:-1] + ')'
        rgb_colors.append(colors)
    return rgb_colors


def generate_colors(n, type):
    if type == 'hexa':
        return list_of_hexa_colors(n)
    elif type == 'rgb':
        return list_of_rgb_colors(n)


print("List of Hexa Colors:")
list_of_hexa = generate_colors(6, 'hexa')
print(list_of_hexa)

print("\nList of RGB Colors:")
list_of_rgb = generate_colors(6, 'rgb')
print(list_of_rgb)
