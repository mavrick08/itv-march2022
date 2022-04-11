"""
if

elif (else if)

else

INDIA
India
india
InDiA
"""

# input_age = int(input("Enter your age "))
# input_country = input("Enter your country name ")
# input_country = input_country.lower()
# if(input_age  >= 18 and input_country == "india"):
#     print("You are eligible to vote")

# else:
#     print("You are not eligible to vote")


# input_time = int(input("Enter Time in 24 hours format "))
# if((input_time>=7 and input_time<=12) or (input_time>=1 and input_time<7)):
#     print("Good Morning")

# elif(input_time>12 and input_time<=17):
#     print("Good Afternoon")

# elif(input_time>17 and input_time<=20):
#     print("Good Evening")

# elif(input_time>20 and input_time<=24):
#     print("Good Night")



# else:
#     print("invalid time")


goal = int(input("Enter Your goal "))
small = int(input("Enter Small Chocolates "))
big = int(input("Enter Big Chocolates "))

if(small+big*5 < goal):
    print("-1")

elif(small < goal % 5):
    print("-1")


else:
    if(goal < 10):
        print(goal%5)
    else:
        print(goal-(big*5))