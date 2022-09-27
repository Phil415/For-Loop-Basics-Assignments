"""
Assignment:
1) Basic
2) Multiples of 5
3) Counting, the Dojo Way
4) Whoa. That Sucker's Huge
5) Countdown by Fours
6) Flexible Counter
"""

for i in range(151):
    print(i)

for i in range(5,1000,5):
    print(i)

def coding_dojo():
    for i in range(1, 101):
        if i % 10 == 0:
            print('Coding Dojo')
        elif i % 5 == 0:
            print('Coding')
        else:
            print(i)

coding_dojo()

def whoa():
    sum=0
    for i in range(1,500001,2):
        sum+=i
    print(sum)

whoa()

def countdown():
    for i in range(2018,0,-4):
        print(i)

countdown()

def flex(lowNumb, highNumb, mult):
    for i in range(lowNumb,highNumb+1):
        if i % mult == 0:
            print(i)

flex(2,9,3)