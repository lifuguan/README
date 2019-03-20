# '''
# Question : 1
# '''
# origin_power = 1.00
# work_counter = 0
# for a in range(1, 366):
#     if work_counter == 10:
#         origin_power = origin_power * 1.01
#         work_counter = 0
#     elif work_counter >= 4:
#         origin_power = origin_power * 1.01
#     work_counter += 1

# print("power is " + str(origin_power))
    
# '''
# Question : 2
# '''
# import turtle  
# import time
# turtle.color("red", "yellow")
# turtle.speed(10)
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
#     turtle.left(170)
# time.sleep(1)

# turtle.penup()
# turtle.goto(-150,-120)
# turtle.color("violet")
# turtle.write("Done", font=('Arial', 40, 'normal'))

'''
Question : 3
'''
origin_a = 0
origin_b = 0
def lowestCommonDivisor(a , b):
    
    b , a = a, b % a  
    if a == 0:
        print(b)
        print(origin_a * origin_b / b)
        return int(b)
    else:
        lowestCommonDivisor(a , b)

origin_a = eval(input())
origin_b = eval(input())
res = lowestCommonDivisor(origin_a, origin_b)
print(res)

def sample(a, b):
    return a + b
print(sample(1 , 2))

'''
input ： 4， 6
output : 2
'''

'''
Question : 4
'''
import math
from math import sqrt
[ p for p in   range(100, 200) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]
'''
output : [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
'''

'''
Question : 5
'''
import math
a = eval(input("input"))
Xn = 1
XnPlus = 0.5 * (Xn + (a / Xn))
while math.fabs(XnPlus - Xn) < 1e-3:
    XnPlus = 0.5 * (Xn + (a / Xn))
    Xn = XnPlus
print(XnPlus)

'''
input : 4
output : 2.5
'''
