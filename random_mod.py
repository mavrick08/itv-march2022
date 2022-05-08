import random

# print(random.randint(1,10))

# print(random.randrange(1,10))

mylist = ['apple','mango','cherry','grapes']
# print(mylist)

# random.shuffle(mylist)

# print(mylist)

# print(random.sample(mylist,k=2))


# print(random.choice(mylist))

print(random.choices(mylist,weights=[6,3,3,2],k=14))

