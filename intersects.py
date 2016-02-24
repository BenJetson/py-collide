#  Copyright (c) 2016 Jon Cooper
#   
#  This file is part of py-collide.
#  Documentation, related files, and licensing can be found at
# 
#      <https://github.com/joncoop/py-collide>.

"""
Parameter definitions for the intersects module:

A point is defined by a list or tuple in the form [x, y] or (x, y).

A circle is defined as a list or tuple in the form [x, y, r] 
where (x, y) represents the center of the circle and r is its radius.

A rect is defined as a list or tuple in the form [x, y, width, height] 
where (x, y) represents the coordinates of the upper left corner of 
the rectangle.
"""


def point_circle(point, circle):
    
    x1 = point[0]
    y1 = point[1]
    x2 = circle[0]
    y2 = circle[1]
    r = circle[2]
    
    return (((x1-x2)**2) + ((y1-y2)**2)) <= r**2
    


def point_rect(point, rect):
    x = point[0]
    y = point[1]
    
    x_min = rect[0]
    y_min = rect[1]
    x_max = rect[0] + rect[2]
    y_max = rect[1] + rect[3]
    
    return (x_min <= x <= x_max) and (y_min <= y <= y_max)


def circle_circle(circle1, circle2):
    
    x1 = circle1[0]
    y1 = circle1[1]
    r1 = circle1[2]
    x2 = circle2[0]
    y2 = circle2[1]
    r2 = circle2[2]
    
    return (((x1-x2)**2) + ((y1-y2)**2)) <= ((r1+r2)**2)


def rect_rect(rect1, rect2):
    
    left1 = rect1[0]
    right1 = rect1[0] + rect1[2]
    top1 = rect1[1]
    bottom1 = rect1[1] + rect1[3]
    
    left2 = rect2[0]
    right2 = rect2[0] + rect2[2]
    top2 = rect2[1]
    bottom2 = rect2[1] + rect2[3]
    
    # return (right1 > left2) or (left2 < right1)# or (top1 > bottom2) or (bottom2 > top1)
    # return not ((right1 < left2) or (top1 > bottom2) or (left1 < right2) or (bottom1 < top2))
    return not ((right1 < left2) or (top1 > bottom2) or (left1 > right2) or (bottom1 < top2))
    