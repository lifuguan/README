#Ex 1 
origin_list = []
for i in range(1, 11):
    origin_list.append(eval(input()))

#Reserve the origin list and output
origin_list.reverse()
print("Reserve ouput : ", origin_list)

#using selection sort
for i in range(0, len(origin_list) - 1):
    min_num = i
    for j in range(i + 1, len(origin_list)):
        if origin_list[min_num] > origin_list[j]:
            min_num = j
    #exchange
    temp = origin_list[min_num]
    origin_list[min_num] = origin_list[i]
    origin_list[i] = temp
print("small to big ouput : ", origin_list)
origin_list.reverse()
print("big to small ouput : ", origin_list)

'''
Reserve ouput :  [11, 2, 4, 3, 5, 8, 7, 6, 9, 1]
small to big ouput :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
big to small ouput :  [11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''

#Ex2
#import numpy as np
origin_list = list(eval(input()))
tot = 0
max_ = 0
min_ = 0
for p in range(len(origin_list)) :
    max_ = max(max_, p)
    min_ = min(min_, p)
    tot += p
ser = eval(input())
counter = 0
for a in origin_list:
    if a == ser:
        counter += 1
print(tot, "  ",max_,  "  ", min_,  "   ", counter)
'''
1,2,3,4
3
6    3    0     1
'''
#Ex3 
dic = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine" : 9,
    "zero": 0
}
input_str = input()
split_list = str(input_str).split(' ')
for a in split_list:
    print(dic[a], end="")
'''
one two three
123
'''

#Ex4

import random
rand_num = random.uniform(0, 100)
for i in range(10):
    guess = int(input())
    if guess< rand_num:
        print("smaller")
    if guess> rand_num:
        print("bigger")
    if guess== rand_num:
        print("Bingo")
#结果
'''
1
smaller
1
smaller
2
smaller
3
smaller
4
smaller
5
smaller
599
bigger
'''

#Ex 5 
D = {"zhangshan": 88, "lisi":90, "wangwu":73, "zhaoliu": 82}
D.update({"qianqi":90})
del D["zhaoliu"]
D["wangwu"] = 93


Ex 6
import random
source = "abcdefghijklmnopqrstuvwxyz0123456789"
length = len(source)
a = []
for i in range(1, 11):
    for j in range(0, 8):
        a.append(source[random.randint(0, length)])
    for k in range(0, 8):
        print(a[k], end="")
    print(a)
    a.clear()
'''
8phfispj['8', 'p', 'h', 'f', 'i', 's', 'p', 'j']
m310zyqy['m', '3', '1', '0', 'z', 'y', 'q', 'y']
f0qkat3v['f', '0', 'q', 'k', 'a', 't', '3', 'v']
mvc4875h['m', 'v', 'c', '4', '8', '7', '5', 'h']
sgpu1izp['s', 'g', 'p', 'u', '1', 'i', 'z', 'p']
xp2y8625['x', 'p', '2', 'y', '8', '6', '2', '5']
gcnea4a8['g', 'c', 'n', 'e', 'a', '4', 'a', '8']
n5i9x9zy['n', '5', 'i', '9', 'x', '9', 'z', 'y']
p9pvc4u7['p', '9', 'p', 'v', 'c', '4', 'u', '7']
z9ogpw64['z', '9', 'o', 'g', 'p', 'w', '6', '4']
'''
