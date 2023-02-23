# - Write a function list_of_hexa_colors which returns any number of hexadecimal colors
#   in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is
#   made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
# Check the task 6 for output examples).
# - Write a function generate_colors which can generate any number of hexa or rgb colors.
#    - generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
#    - generate_colors('hexa', 1) # ['#b334ef']
#    - generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
#    - generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


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


def generate_colors(type, n):
    if type == 'hexa':
        return list_of_hexa_colors(n)
    elif type == 'rgb':
        return list_of_rgb_colors(n)


print("List of Hexa Colors:")
list_of_hexa = generate_colors('hexa', 6)
print(list_of_hexa)

print("\nList of RGB Colors:")
list_of_rgb = generate_colors('rgb', 6)
print(list_of_rgb)

print(generate_colors("hexa", 3))
print(generate_colors("hexa", 1))
print(generate_colors("rgb", 3))
print(generate_colors("rgb", 1))
