# lists are similar to arrays

mylist = []
mylist.append(1)
mylist.append(2)
print(mylist[0])
print(mylist[1])

# iterate
for x in mylist:
    print(x)

# exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")
second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)