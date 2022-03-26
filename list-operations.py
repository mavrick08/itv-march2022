mylist = ["hello","hola","tata","see you"]
print(len(mylist))  #this will calculate the length of your list 

mylist.append("bye")
print(mylist)
mylist.insert(1,"dummy")
print(mylist)

mylist.clear()
print(mylist)

mylist = ["hello","hola","tata","see you"]
print(mylist)
# print(mylist.pop())
# print(mylist)
print(mylist.pop(0))
print(mylist)
mylist.remove('tata')
print(mylist)

numbers = [10,20,0,40,33,66,88,100,2,7]
numbers.sort(reverse=True)
print(numbers)

city = ["mumbai","chennai","delhi","ahmedabad","jaipur"]
city.sort()
print(city)


numbers = [55,10,1000,400,500]
numbers.reverse()
print(numbers)

print(numbers.count(1000))

# print(numbers.index(7000))

copied_lst = numbers.copy()

print(copied_lst)

numbers.append("hello")


# copied_list2 = numbers
# print(copied_lst)
# print(numbers)

print(numbers)

numbers.extend(["c","c++","php","python"])

print(numbers)


numbers.append(["cricket","swimming","cooking"])

print(numbers)