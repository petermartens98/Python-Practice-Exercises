# Area of a triangle
# Write a function that takes the base and height of a triangle and return its area.
# Difficulty: Very Easy
# Date: 8/5/2021

base = int(input("Enter the base of your triangle: "))
height = int(input("Enter the height of your triangle: "))

def triangle_area(base,height):

    area = base*height
    area = area/2
    return area

print("The area of this triangle is: "+str(triangle_area(base,height)))

