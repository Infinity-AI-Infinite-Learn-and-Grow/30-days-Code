"""Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
Write a function generate_colors which can generate any number of hexa or rgb colors.
generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3) # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
generate_colors('rgb', 1) # ['rgb(33,79, 176)'] """

import random

def list_of_hexa_colors(n):
    """Returns any number of hexadecimal colors in an array"""
    return [f'#{random.randint(0, 0xFFFFFF):06X}' for i in range(n)]  
def generate_colors(color_type, n):

    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return [f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})' for i in range(n)]
    else:
        return None

if __name__ == '__main__':
    print(generate_colors('hexa', 1))
    print(generate_colors('hexa', 3))
    print(generate_colors('rgb', 3))
    print(generate_colors('rgb', 1))