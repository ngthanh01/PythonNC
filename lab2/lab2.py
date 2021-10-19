#Chương 8
#Bài 1
kingdoms =  ['Bacteria', 'Protozoa', 'Chromista','Plantae', 'Fungi', 'Animalia']
#câu a
print(kingdoms[0])
#câu b
print(kingdoms[5])
#câu c
print(kingdoms[:3])
#câu d
print(kingdoms[2:5])
#câu e
print(kingdoms[4:])
#câu f
print(kingdoms[1:0])

#Bài 2
#câu a
print(kingdoms[-6])
#câu b
print(kingdoms[-1])
#câu c
print(kingdoms[-6:-3])
#câu d
print(kingdoms[-4:-1])
#câu e
print(kingdoms[-2:])
#câu f
print(kingdoms[-1:-2])

#Câu 3
appointments =  ['9:00', '10:30', '14:00', '15:00','15:30']
#câu a
appointments.append('16:30')
print(appointments)
#câu b
appointments += ['16:30']
print(appointments)
#câu c
# append sửa đổi danh sách, còn + đã tao ra danh sách mới

#Câu 4
list =  [4353, 2314, 2956, 3382, 9362, 3900]
#a
list.remove(3382)
#câu b
print(list.index(9362))
#câu c
list.insert(4,4499)
print(list)
#câu d
list.extend([5566,1830])
print(list)
#câu e
list.reverse()
print(list)
#câu f
list.sort()
print(list)

#câu 5
#câu a
list =  [4, 12,20,38,56,88]
alkaline_earth_metals = list
print(alkaline_earth_metals)
#câu b
print(alkaline_earth_metals[5]) 
print(alkaline_earth_metals[-1])
#câu c
print(len(alkaline_earth_metals))
#câu d
print(max(alkaline_earth_metals))#tìm phần tử lớn nhất
#câu 6
#câu a
list = [25.2,16.8,31.4,23.9,28,22.5,19.6]
temps=list
print(temps)
#câu b
temps.sort()
print(temps)

#câu c
cool_temps = temps[0:2]
warm_temps = temps[2:]
print(cool_temps)
print(warm_temps)
#câu d
temps_in_celsius = cool_temps+warm_temps
print(temps_in_celsius)

#câu 7
def same_first_last(L) :
    return L[0] == L[-1]
print(same_first_last([3, 4, 2, 8, 3]))
print(same_first_last(['apple', 'banana', 'pear']))
print(same_first_last([4.0, 4.5]))

#câu 8
def is_longer(L1, L2):
    return len(L1) > len(L2)
print(is_longer([1, 2, 3], [4, 5]))
print(is_longer(['abcdef'], ['ab', 'cd', 'ef']))
print(is_longer(['a', 'b', 'c'], [1, 2, 3]))

#câu 9
values = [0, 1, 2]
values[1] = values
print(values)

#câu 10
list =  [['km', 'miles', 'league'], ['kg', 'pound','stone']]
print(list[0])
print(list[-1])
print(list[0][0])
print(list[1][0])
print(list[0][1:3])
print(list[1][0:2])

#câu 11
print(list[-2])
print(list[-1])
print(list[-2][-3])
print(list[-1][-3])
print(list[-2][-2:])
print(list[-1][0:-1])

#Chương 9
#câu 1
celegans_phenotypes =  ['Emb','Him', 'Unc', 'Lon', 'Dpy', 'Sma']
for phenotype in celegans_phenotypes:
    print(phenotype)

#câu 2
#in ra danh sách
half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
for value in half_lives:
    print(value, end='!')

#câu 3
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = []
for count in whales:
    more_whales.append(count + 1)
print(more_whales)

#câu 4
#a
list = [[4, 9.012], [12, 24.305],[20, 40.078], [38, 87.62],[56, 137.327], [88, 226]]
alkaline_earth_metals = list
print(alkaline_earth_metals)

#b
for element in alkaline_earth_metals:
    print('atomic number: ', element[0])
    print('atomic weight: ', element[1])
    print('')
#c
number_and_weight = []
for element in alkaline_earth_metals:
    number_and_weight.append(element[0])
    number_and_weight.append(element[1])
print('number_and_weight: ', number_and_weight)
#5  add  a docstring, type annotations, or comments
def mystery_function(values):
    """ Trả về một bản sao có các danh sách con.
    Phần từ trong danh sách con được đảo ngược
    >>> mystery_function([[1,2,3], [4,5,6]])
    [[3,2,1],[4,5,6]
     """
    result = []
    for sublist in values:
        result.append([sublist[0]]) # result = [[1]] 
        for i in sublist[1:]: # lan 1: i = 2,3  / lan 2: i = 5,6  
            result[-1].insert(0, i) 
            # them i vao truoc.
            # Lan 1. result[-1] = [1]
            # Lan 2. result[-1] = [4]
    return result
print( mystery_function([[1, 2, 3], [4, 5, 6]]))

print("--------/////--------")
#6 type quit (any capitalization) to exit
text = ""
while text.lower() != "quit":
    text = input("Please type quit (any capitalization) to exit: ")
    if text.lower() == "quit":
        print("Exited program")

print("--------/////--------")
#7 add the population of the current country to total
country_populations = [1295, 23, 7, 3, 47, 21]
total = 0
for population in country_populations:
    total += population
print('total population = ', total)

print("--------/////--------")
#8
rat_1 = [2,1,3,4,7,6,2,3,5,8]
rat_2 = [1,3,2,2,6,8,4,2,2,9]
#8a
if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1.")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")
#8b
if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
    print("Rat 1 remained heavier than Rat 2.")
else:
    print("Rat 2 became heavier than Rat 1.")
#8c
if rat_1[0] > rat_2[0]:
    if rat_1[-1] > rat_2[-1]:
        print("Rat 1 remained heavier than Rat 2.")
    else:
        print("Rat 2 became heavier than Rat 1.")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")

print("--------/////--------")
#9  Print the numbers in the range 33 to 49 (inclusive)
for number in range(33, 50):
    print(number)

print("--------/////--------")
#10 Print the numbers from 1 to 10 (inclusive) in descending order, all on one line.
for number in range(10):
    print(10 - number, end=' ')
print('')

print("--------/////--------")
#11
sum = 0
count = 0
for number in range(2,23):
    sum += number
    count += 1
average = sum / count
print('sum = ', sum)
print('count = ', count)
print('average = ', average)

print("--------/////--------")
#12 Rewrite the code 
def remove_neg(num_list):
    index = 0
    while index < len(num_list):
        if num_list[index] < 0:
            num_list.remove(num_list[index])
        else:
            index += 1
num_list = [1, 2, 3, -3, 6, -1, -3, 1]
remove_neg(num_list)
print(num_list)

print("--------/////--------")
#13 a right triangle
for width in range(1, 8):
    print('T' * width)

print("--------/////--------")
#14 a right triangle with s hypotenuse on the left side
for width in range(1, 8):
    print(' '*(7 - width), 'T'* width)

print("--------/////--------")
#15 Redo the previous two exercises using while loops instead of for loops.
width1 = 1
while width1 < 8:
    print('T' * width1)
    width1 += 1

width2 = 1
while width2 < 8:
    print(' '*(7 - width2), 'T'*width2)
    width2 += 1

print("--------/////--------")
#16
rat_1_weight = [2,1,1,4,5,7,2,3,5,8];
rat_2_weight = [2,1,1,4,6,6,4,2,2,9];
#16a how many weeks the weight of the first rat to become 25 percent heavier 
week = 0
while rat_1_weight[week] / rat_1_weight[0] - 1 < .25:
    week += 1
print(week)
#16b  how many weeks it would take for rat 1 to be 10 percent heavier than rat 2
week = 0
while rat_1_weight[week] / rat_2_weight[week] - 1 < .10:
    week += 1
print(week)









