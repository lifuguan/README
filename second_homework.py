# Ex 1
num = input()
sum_val = 1
for i  in range(int(num)+1) :
    if i == 0:
        pass
    else:
        sum_val *= i
print(sum_val)

#结果
'''
cd c:\Users\10027\Desktop && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe" c:\Users\10027\.vscode\extensions\ms-python.python-2019.2.5558\pythonFiles\ptvsd_launcher.py --default --nodebug --client --host localhost --port 13335 c:\Users\10027\Desktop\hello.py "
3
6
'''

# Ex 2 

'''
# 有趣， Python很简单的.jpg
from math import sqrt    
N = 100   
[ p for p in   range(2, N) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]    
'''
num = eval(input())
def isPrime(n): 
  if n <= 1: 
    return False
  i = 2
  while i*i <= n: 
      if n % i == 0: 
       return False
    i += 1
  return True
if isPrime(num) == True:
    print("Bingo")

#答案
'''
2
Bingo
'''



# EX 3
num = 1
for x in range(1, 100):
    for y in range(1, 100):         
        if (100 -x -y) % 9 == 0:
            z = (100 - x - y) / 9
            if (2 * x + 4 * y + 2 * z) == 100:
                print("list "+str(num) + " ")
                print(x, end="\n")
                print(y, end="\n")
                print(z, end="\n")
                num += 1
#结果
'''
list 1 :
14
14
8.0
list 2 :
31
6
7.0
'''

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
num_nul = 0
num_int = 0
num_low = 0
num_capital = 0
num_other = 0
str = input()
for i in str:
    ans_IN = ord(i)
    if ans_IN >=48 and ans_IN <= 57:
        num_int += 1
    elif ans_IN >= 65 and ans_IN <= 90:
        num_capital += 1
    elif ans_IN >= 97 and ans_IN <= 122:
        num_low += 1
    elif ans_IN == 32:
        num_nul += 1
    else:
        num_other += 1
print(num_int)
print(num_capital)
print(num_low)
print(num_nul)
print(num_other)

#结果
'''
>>> print(num_int)
6
>>> print(num_capital)
2
>>> print(num_low)
5
>>> print(num_nul)
0
>>> print(num_other)
4
'''
