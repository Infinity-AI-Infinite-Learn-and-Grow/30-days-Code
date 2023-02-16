import random
l=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def list_of_hexa_colors(n):
    t=()
    for i in range(n):
        f = ('#'+random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l),)
        t = t+f
    print(t)


def rgb_colour(n):
    s = []
    for i in range(n):
        t = ('rgb'+'('+str(random.randrange(0, 256))+','+str(random.randrange(0, 256))+','+str(random.randrange(0, 256)),)
        s.extend(t)
    print(s)


def generate_colors(p = "hexa", n=0):
    if(p == "hexa"):
        list_of_hexa_colors(n)
    elif(p == "rgb"):
        rgb_colour(n)
    else:
        print("wrong choice have been made")
generate_colors("hexa",3)
generate_colors("hexa",1)
generate_colors("rgb",3)
generate_colors("rgb",1)
