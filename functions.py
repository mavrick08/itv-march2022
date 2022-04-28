# def greet():
#     print("Hi Welcome to Functions")


# greet() #calling the function 
# print(greet()) #printing the function call

# def greet():
#     return "Hi Welcome to functions"

# print(greet())


# def info():
#     name = "steve"
#     age = 29
#     loc = "mumbai"
#     print(f'Name is {name} Age is {age} Location is {loc}')


# info()
# print(name)


# def info(name,age,loc):
#     print(name)
#     print(age)
#     print(loc)


# info("Punit",29,"Mumbai")


# def foo_info(name,age):
#     """
#     This function takes 2 input name and age
#     It prints the data back to the user and shows the output
#     """
#     print(name)
#     print(age)

# foo_info()

# # foo_info(52,"steve")
# foo_info(age=52,name='steve')


# def info_data(name,age,city):
#     print(f'Your Name is {name}')
#     print(f'Your Age is {age}')
#     print(f'Your City is {city}')

# inp_name = input("Enter Your Name ")
# inp_age = int(input("Enter your age "))
# inp_city = input("Enter Your city ")

# info_data(inp_name,inp_age,inp_city)


# def citizen_info(name,age,country="India"):
#     print(name)
#     print(age)
#     print(country)

# citizen_info("Punit",29,"USA")

# local and global 

# city_name = "mumbai"  #global variable
# def print_city():
#     print(f'Accessing inside function body {city_name}')

# print_city()
# print(city_name)


city = "new york"   #global variable

# def city_info():
#     city = "mumbai"  #local varibale
#     print(city)

# city_info()
# print(city)

def city_info2():
    global city
    city = "Pune"
    print(f'Printing in local variable {city}')


city_info2()
print(f'Printing outside function {city}')





