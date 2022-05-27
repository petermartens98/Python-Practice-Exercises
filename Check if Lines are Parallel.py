# Check if Lines are Parallel
# Given two lines, determine whether or not they are parallel.
# Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.
# Examples:
#    lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ True
#    x+2y=3 and x+2y=4 are parallel.
#
#    lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ False
#    2x+4y=1 and 4x+2y=1 are not parallel.
# Difficulty: Medium
# Date: 8/7/2021

a = 0
b = 0
c = 0
line1 = [a,b,c]
line2 = [a,b,c]

def parallel (line1, line2):

    line1slope = int(line1[a]/line1[b])
    line1slope = line1slope * (-1)


    line2slope = int(line2[a] / line2[b])
    line2slope = line2slope * (-1)


    if line1slope == line2slope:
        print("Lines are parallel")

    else:
        print("These lines are not parallel")


line1 = [1,2,3]
line2 = [1,2,4]

parallel(line1,line2)