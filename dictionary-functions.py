from xxlimited import foo


my_dict = {
    "name":"punit",
    "age":29,
    "qual":"MCA",
    "loc":"Khar"
}

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# my_dict.clear()
# print(my_dict)
# new_dict = my_dict.copy()
# print(new_dict)

# copy_dict = my_dict
# print(copy_dict)
# print(my_dict.pop('loc'))
# print(my_dict)

# print(my_dict.popitem())
# print(my_dict)

my_dict['designation'] = "Data Engineer"

# print(my_dict)

my_dict.update({'designation':'Python Developer'})

# print(my_dict)

my_dict.update({'food':'South Indian'})

# print(my_dict)

# print(my_dict.get('name'))

# info = {}
# info.setdefault('Gender')
# print(info)

mykeys = ('key1','key2','key3','key4')
val = "test"
foo_dict = dict.fromkeys(mykeys,val)
print(foo_dict)

