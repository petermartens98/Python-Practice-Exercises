# Length of Line Segment
# Write a function that takes coordinates of two points on a two-dimensional plane
# and returns the length of the line segment connecting those two points.
# Example:
#   line_length([15, 7], [22, 11]) ➞ 8.06
#   line_length([0, 0], [0, 0]) ➞ 0
#   line_length([0, 0], [1, 1]) ➞ 1.41
# Difficulty: Medium
# Date: 8/7/2021

import math

x=0
y=0

point1 = [x, y]
point2 = [x, y]

def line_length(point1, point2):


    x1 = int(point1[x])
    y1 = int(point1[y])
    x2 = int(point2[x])
    y2 = int(point2[y])

    xcomp = abs(x1 - x2)
    xcomp = xcomp * xcomp

    ycomp = abs(y1 - y2)
    ycomp = ycomp * ycomp

    length = xcomp + ycomp
    length = math.sqrt(length)


    print(str(length))

point1=[0,0]
point2=[1,1]
line_length(point1,point2)



