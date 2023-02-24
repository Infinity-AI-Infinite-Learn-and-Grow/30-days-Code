#Day 12

import random

# ------Task 1------
hexa_list=[]
rgb_list=[]
def list_of_hexa_colors(num):
    for i in range(num):
        random_number = random.randint(0,16777215)
        hex_number = str(hex(random_number))
        hex_number ='#'+ hex_number[2:]
        hexa_list.append(hex_number)
    print("Hexadecimal colours are",hexa_list)

list_of_hexa_colors(random.randint(0,10))
print("\t")

# ------Task 2------
hexa_list=[]
rgb_list=[]
def generate_colors(color_type,num):
    if(color_type=="hexa"):
        for i in range(num):
            random_number = random.randint(0,16777215)
            hex_number = str(hex(random_number))
            hex_number ='#'+ hex_number[2:]
            hexa_list.append(hex_number)
        print("Hexa color list :",hexa_list)
    else:
        for i in range(num):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            rgb = (r,g,b)
            rgb_list.append(rgb)
        print("RGB colour list : ",rgb_list)


generate_colors("hexa",3)
generate_colors("rgb",3)
