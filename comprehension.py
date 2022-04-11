'''
[expression loop condition]
'''

# sq_lst  = [item**2 for item in range(1,11)]
# print(sq_lst)


# odd_lst = [num for num in range(1,101) if num % 2 !=0]
# print(odd_lst)

cube_dict = {num:num**3 for num in range(1,11)}
print(cube_dict)


cities = ['Mumbai','Chennai','Delhi','Jaipur','Pune']


city_dict = {item:len(item) for item in cities}
print(city_dict)

