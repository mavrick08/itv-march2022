# for item in range(1,11,2):
#     print(item)

# for item in range(10,0,-1):
#     print(item)


"""
0+1 = 1
2+1 = 3
3+3 = 6
4+6 = 10
5+10 = 15
6+15 = 21
7+21 = 28
8+28 = 36
9+36 = 45
10+45 = 55
"""

# total = 0
# for num in range(1,11):
#     total = total + num
# print(total)

"""
p
i
n
e
a
p
p
l
e
"""
from numpy import average


fruit = "pineapple"    #ieae

# for char in range(0,len(fruit)):
#     print(char,fruit[char])

# for item in fruit:
#     print(item.upper())


# for char in range(0,len(fruit)):
#     if(fruit[char] == 'a' or fruit[char] == 'e' or fruit[char] == 'i' or fruit[char] == 'o' or fruit[char] == 'u'):
#         print(fruit[char])


# vowels = ['a','e','i','o','u']

# for item in fruit:
#     if item in vowels:
#         print(item)

# hobbies = ['cricket','swimming','cooking','travelling']

# for items in range(0,len(hobbies)):
#     print(items,hobbies[items])

# my_sq_list = []

# for num in range(1,11):
#     my_sq_list.append(num**2)
# print(my_sq_list)

# my_vowels = []
# for char in range(0,len(fruit)):
#     if(fruit[char] == 'a' or fruit[char] == 'e' or fruit[char] == 'i' or fruit[char] == 'o' or fruit[char] == 'u'):
#         my_vowels.append(fruit[char])
# print(my_vowels)

# student_marks_list = []

# inp_subject = int(input("How many subjects do you have "))

# for inp_marks in range(1,inp_subject+1):
#     marks = int(input("Enter Your Marks "))
#     student_marks_list.append(marks)

# total = 0
# for items in student_marks_list:
#     total = total + items

# average = total/len(student_marks_list)
# print(f'Average is {average}')

# mytup = ('mumbai','pune','delhi','chennai')

# for val in range(0,len(mytup)):
#     print(val,mytup[val])

# for items in mytup:
#     print(items)

# mydict = {
#     "name":"punit",
#     "age":29,
#     "location":"Mumbai"
# }

# for key in mydict.keys():
# #     print(key)


cube_dict = {}

for item in range(1,11):
    cube_dict[item] = item ** 3

print(cube_dict)


# for val in mydict.values():
#     print(val)

# for k,v in mydict.items():
#     print(k,v)



# my_set = {10,20,30,40,50,60,70,80,90}

# for val in my_set:
#     print(val)

new_set = set()

for item in range(1,31):
    if item % 2 == 0:
        new_set.add(item)

print(new_set)