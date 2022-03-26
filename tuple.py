"""
we can define the tuple by using the 'tuple' keyword
OR we can define by using the () symbol
"""

mytuple = (100,200,300,400,500,100,200)
# print(mytuple)


# print(mytuple.count("hello"))

print(mytuple.index(200))


'''
storing a list in a tuple
'''

mixed = (10,20,30,["steve","alpha","beta","gamma"])
print("Before addition Length is",len(mixed))
# print(mixed[3])
# print(mixed.append(50))
mixed[3].append("demo")
print("Length after addition is",len(mixed))


"""
creating tuple inside a list
"""

mixed_l = [
    (100,200,300,400,500),
    "hello","bye"
]
print(mixed_l[2])
mixed_l.append("demo")



# mytup = (100,200,300,400,100)

mylist = [100,200,300,400,500,100]

# print(mylist[1:4])

print(mylist[4:6].index(100))

print(mytuple[1:6])

print("----------------------\n")
print(mylist)

print(mylist.index(100,2,6))