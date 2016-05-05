#  Copyright (c) 2016 Jon Cooper
#   
#  This file is part of py-collide.
#  Documentation, related files, and licensing can be found at
# 
#      <https://github.com/joncoop/py-collide>.

import pygame

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
    a = point[0] - circle[0]
    b = point[1] - circle[1]
    r = circle[2]

    return a**2 + b**2 <= r**2
    

def point_rect(point, rect):
    x = point[0]
    y = point[1]

    left = rect[0]
    right = rect[0] + rect[2]
    top = rect[1]
    bottom = rect[1] + rect[3]

    return left <= x <= right and top <= y <= bottom
    

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

    return not (right1 < left2 or
                left1 > right2  or
                bottom1 < top2 or
                top1 > bottom2)


def rect_absorbs_rect(rect1, rect2):
    
    left1 = rect1[0]
    right1 = rect1[0] + rect1[2]
    top1 = rect1[1]
    bottom1 = rect1[1] + rect1[3]

    left2 = rect2[0]
    right2 = rect2[0] + rect2[2]
    top2 = rect2[1]
    bottom2 = rect2[1] + rect2[3]
    
    return ((left1 >= left2 and right1 <= right2 and top1 >= top2 and bottom1 <= bottom2) or
            (left2 >= left1 and right2 <= right1 and top2 >= top1 and bottom2 <= bottom1))


def percent_points_touching(object1, object2, percent):

    percent /= 100

    object1mask = pygame.mask.from_surface(object1.image)
    object2mask = pygame.mask.from_surface(object2.image)

    overlap1 = object1mask.overlap_area(object2mask, (abs(object1.x - object2.x), abs(object1.y - object2.y)))
    overlap2 = object2mask.overlap_area(object1mask, (abs(object1.x - object2.x), abs(object1.y - object2.y)))

    count1 = object1mask.count()
    count2 = object2mask.count()

    if (overlap1 > (count1 * percent) or
            overlap1 > (count2 * percent) or
            overlap2 > (count1 * percent) or
            overlap2 > (count2 * percent)):
        return True
    else:
        return False
