from sympy import *

'''
Center (h,K)
R is radius
(distance from center to edge of circle)
(X-h)**2+(y-k)**2=r**2
'''

'''
example 1 Identify center and radius
(x-3)**2+(y-2)**2=4

example 2
(x+3)**2+(y-2)**2=13

example 3
(x+3)**2+(y+2)**2=1
'''

'''
example 1
center is (3,2) They change signs from the equations. h = 3 and k = 2.
radius is 2, because sqrt(4) is 2.

example 2
center is (-3,2)
radius is r**2 = 13. so sqrt(13)

example 3
center is (-3,-2)
radius is sqrt(1) or 1
'''

'''
find the equation of the circle
center = (3,0)
point = (3,2)
answer needs to be (x-h)**2 + (y-k)**2 = r**2
so (x-3)**2 + (y-0)**2 = r**2
still need to find r.
x are the same but y is different by 2.
r = sqrt(4) or 2
'''

'''
try 
center= (2,1)
point = (0,1)
(x-2)**2 + (y-1)**2 = 2**2

center at origin
circle contains the point (-9,1)
origin is (0,0)

so far (x-0)**2 + (y-0)**2 = r**2 or x**2 + y**2 = r**2
use distance formula for r.
so sqrt((2nd x = 1st x)**2 + (2nd y - 1st y)**2)
so sqrt( (0-(-9))**2 + (0-1)**2  ) = sqrt(82)
so r = 82
so x**2 + y**2 = 82

'''
# print(
#     sqrt( (0-(-9))**2 + (0-1)**2  )
# )

# fairly simple. Just the formula for distance.
def find_r(first_x, first_y, second_x, second_y):
    r = nsimplify(
        sqrt(
            (second_x - first_x)**2 + (second_y - first_y)**2
        )
    )

    print(
        f'r = {r} \nr2 = {r**2}'
    )
# find_r(-9,1,0,0)

'''
try
center (2,3)
point (1,4)

(x-2)**2 + (y-3)**2 = sqrt(2)
'''
# find_r(1,4,2,3)


'''
find the equation of a circle with
point 1 = (1,8)
point 2  = (10,8)
(1st x + 2nd x)/2, (1st y + 2nd y)/2 = (11/2,8)
so (x=11/2)**2 + (y-8)**2 = r**2
'''
# find_r(1,8,11/2,8)

'''
(5,6) (-3,4)
'''
# question gives 2 "END" points and neither are the center.
# finds the center using the formula for midpoint
def find_center(first_x, first_y, second_x, second_y):
    center_x = nsimplify((first_x + second_x)/2)
    center_y = nsimplify((first_y + second_y)/2)
    print(f'center = ({center_x}, {center_y})')
    # now that we have center, we can find the radius using it and any previous point. We just use the first.
    find_r(center_x, center_y, first_x, first_y)
# find_center(5,6,-3,4)

# find_r(2,-8,0,0)

# find_center(4,8,15,8)

'''
example:
find the standard form of the circle that endpoints of a diameter (1,6) and (7,6)

answer:
(x-4)**2 + (y-6)**2 = 9
'''
find_center(1,6,7,6)


