# Chương 3
# 1a
a = min(2,3,4)
print("min: ",a)
# 1b 
b = max(2, -3, 4, 7, -5)
print("max: ",b)
# 1c 
c = max(2, -3, min(4, 7), -5)
print("max: ",c)

#2a
a = min(max(3, 4), abs(-5))
print("min: ",a)
#2b
b = abs(min(4, 6, max(2, 8)))
print("abs: ",b)
#2c
c = round(max(5.572, 3.258), abs(-2))
print("round: ",c)

#3 function: num*3
def triple(num):
 return num * 3
print(triple(2))

#4 function: 2 num , abs
def absolute_difference(number1, number2):
 return abs(number1 - number2)
print(absolute_difference(1,5))

#5 function: km -> miles
def km_to_miles(km):
 return km / 1.6
print(km_to_miles(10))

#6 function: 3num, average
def average_grade(grade1, grade2, grade3):
 return (grade1 + grade2 + grade3) / 3
print(average_grade(2,3,4))

#7 function: 4num, average of 3 max num
def top_three_avg(grade1, grade2, grade3, grade4):
    total = grade1 + grade2 + grade3 + grade4
    top_three = total - min(grade1, grade2, grade3, grade4)
    return top_three / 3
print(top_three_avg(50,60,70,80))

 #other solution
def top_three_avg_2(grade1, grade2, grade3, grade4):
    return max(average_grade(grade1, grade2, grade3),
           average_grade(grade1, grade2, grade4),
           average_grade(grade1, grade3, grade4),
           average_grade(grade2, grade3, grade4))
print(top_three_avg_2(50,60,70,80))

#8 day1 and day2 are days in the same year. Return the number of full weeks
#that have elapsed between the two days.
def weeks_elapsed(day1, day2):
    days = max(day1,day2) - min(day1,day2)
    weeks = days // 7;
    return weeks
print(weeks_elapsed(20,3))

#9 #10 : function: square of num
def square(num):
    return num ** 2
print(square(4))


#Chương 6:
import math

#1a 
print(math.floor(-2.8))
#1b
print(abs(round(-4.3)))
#1c
print(math.ceil(math.sin(34.5)))

#2a 2b
import calendar
#2c
print(help(calendar.isleap))
#2d
print(calendar.isleap(2021))
#2e
print(dir(calendar))
#2f
print(calendar.leapdays(2000, 2050))
#2g
print(calendar.weekday(2016, 7, 29))

#3 Import file
from exercise import *
#3a
print(average(10,20))
#3b
def average(num1: float, num2: float):
    return (num1 + num2)/2
print(average(10,20)) 



#Chương 7:
#1a
print('hello'.upper())
#1b
print('Happy Birthday!'.lower())
#1c
print('WeeeEEEEeeeEEEEeee'.swapcase())
#1d
print('ABC123'.isupper())
#1e
print('aeiouAEIOU'.count('a'))
#1f
print('hello'.endswith('o'))
#1g
print('hello'.startswith('H'))
#1h
print('Hello {0}'.format('Python'))
#1i
print('Hello {0}! Hello {1}!'.format('Python', 'World'))

#2 number of o’s in 'tomato'
print("number of o's in tomato: ",'tomato'.count('o'))

#3 index of first 'o' in 'tomato'
print("index of first o's in tomato: ",'tomato'.find('o'))

#4 index of second 'o' in 'tomato'
x = 'tomato'.find('o')
print("index of second o's in tomato: ",'tomato'.find('o',x+1))
    
#5 index of second 'o' in 'avocado'
x = 'avocado'.find('o')
print("index of second o's in avocado: ",'avocado'.find('o',x+1))

#6 replace 'n' in 'runner' into 'b'
print('runner ->', 'runner'.replace('n','b'))

#7 strip()

#8a fruit.count() -> fruit.find()
#8b fruit.upper() -> .swapcase() -> fruit.count()
#8c frui.swapcase() -> fruit.lower() -> fruit.replace

#9
season = 'summer'
print('I love {0}!'.format(season))

#10
side1 = 3
side2 = 4
side3 = 5
print('The sides have lengths {0}, {1}, and {2}.'.format(side1, side2, side3))

#11a 
print('boolean'.capitalize())
#11b 
print('CO2 H2O'.find('2'))
#11c 
print('CO2 H2O'.find('2', 'CO2 H2O'.find('2') + 1))
#11d
print('Boolean'[0].islower())
#11e
print("MoNDaY".lower().capitalize())
#11f
print(" Monday".lstrip())

#12
def total_occurrences(s1, s2, ch):
    """ (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    return s1.count(ch) + s2.count(ch)
print(total_occurrences('Thanh','Binh','n'))