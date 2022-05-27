# Perimeter of a Triangle
# Write a function that takes the coordinates of three points in the form of a 2d array and returns
# the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.
# Example:
#   perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08
#   perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.42
#   perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28
# Difficulty: Hard
# Date: 8/8/2021

pointa = [0,0]
pointb = [0,0]
pointc = [0,0]

def perimeter(pointa,pointb,pointc):
    ax = pointa[0]
    bx = pointb[0]
    cx = pointc[0]

    ay = pointa[1]
    by = pointb[1]
    cy = pointc[1]

    def lowesty (ay,by,cy):
        if ay > by > cy or by > ay > cy:
            lowesty = cy
        elif ay > cy > by or cy>ay>by:
            lowesty = by
        else:
            lowesty = ay

        return lowesty

    lowy = lowesty(ay,by,cy)

