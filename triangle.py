def is_triangle(a, b, c):
    if a > b + c or (b > a + c) or (c > a + b):
        print ("No! You can not make a triangle!")
    else:
        print ("Yes! You can make a triangle.")

is_triangle(2, 2, 2)
