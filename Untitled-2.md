# 2019.3.6 The second homework for Python

### Question one
``` python
'''
Q alpha
'''
a = input()
b = input()

if int(a) > int(b):
    print(a)
else:
    print(b)
```
### Question two
```python
'''
Q bravo
'''
year_ = input()
if a % 4 == 0 and a % 100 != 0:
    print("confirm")
elif a % 100 == 0 and a % 400 == 0:
    print("confirm")
else:
    print("OUT")
```

### Question three
```python
'''
Q C
'''
gd = input()
if gd >= 90:
    print("youxiu")
elif gd >= 80:
    print("lianghao")
elif gd>=70:
    print("zhongdeng")
elif gd >= 60:
    print("hege")
else:
    print("You fucking failed")
```

### Question four
```python
'''
Q D
'''
num = input()
if num % 105 == 0:
    print("can be divided by 3, 5 and 7 ")
elif num % 15 == 0:
    print("can be divided by 3 and 5")
elif num % 35 == 0:
    print("can be divided by 5 and 7")
elif num % 21 == 0:
    print("can be divided by 3 and 7")
else :
    print("can be divided by nothing")
```

### Question five
```python
'''
Q E
'''
IN = input()

ans_IN = ord(IN)
if ans_IN >=48 and ans_IN <= 57:
    print("it's a number")
elif ans_IN >= 65 and ans_IN <= 90:
    print("it's a capital letter")
elif ans_IN >= 97 and ans_IN <= 122:
    print("it's a lower case")
else:
    print("Others")
```