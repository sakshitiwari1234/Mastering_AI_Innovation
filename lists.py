# Lists are ordered  , mutable , collection of items. They can contain items of different data type. 

lst= []
print(type(lst))

# LIST IS defined by naming a veriable and then iniltilizing putting items inside the square brackets. 
names = ["sakshi" , "aditya " , "tanushree" , "anurag"  ,"ajay"]

mixed_lists = ["kirsh" , "jack" , 1 , 4]

# accessing list items

fruits = ["apple" , "banana" , "cherry" , "pemgranate", "kiwi" , "mango" , "gauava"]


print(fruits[2])
print(fruits[1:])

print(fruits[1:3])

print(fruits[-1])

print(fruits[-1:-3])

# modify list items

print(fruits)

fruits[1:] = 'watermelon'
print(fruits)

# list methods

fruits.append("orange")
print(fruits)

fruits.insert(1, "banana")
print(fruits)

# remove removes the first occurence 

# remove and return the last

new_fruits = fruits.pop()
print(new_fruits)

print(fruits)

index = fruits.index("apple")
print(index)


# sorting

fruits.sort()
print(fruits)


fruits.reverse()
print(fruits)


fruits.clear()
print(fruits)

# Slicing list
numbers = [1,2,3,4,5,6,7,8]

print(numbers[2:5])
print(numbers[:5])

# in slicing , negative sign simply mean that , .. it start printing form back



# iterting over lists 

for i in numbers :
    print(i)
    
    
    
# iterate with index

for index, number in enumerate(numbers):
    print(index , numbers)
    
    
# list comprehension

list1 = []
for x in range(10):
    list1.append(x*2)
    
print(list1)
    


# list3 = [x**2  for in range(20)]
# print(list3)

# list comprehension

# basicx syntax                 [ expression for item in iterable]
# with conditionla logic        [expression for item in iterable , if conditon]

# basic 

square = [num**2 for num in range(10)]
print(square)


# converting even odd numvres prinint with help of if condition through list complreshention
num = 0 
list4 =[num for i in range(10) if num%2==0 ]
print(list4)



# Nested list comprehension

lt5= [1,2,3,4]
lt6 = ['a' , 'b' , 'c', 'd', 'e']

pair = [[i,j] for i in lt5 for j in lt6]
print(pair)


# list compreshension with function calls

words = [ "hello" , "sakshi" , "how" , "are"  , "you"]

lengths = [len(word) for word in words]
print(lengths) 



#  list is sometihgn very important , and also list compreshension , are a powerful and concise way to create lists in python , they are sybntacitcaly compact adn can replace more verbose looping constructs. 

# learning the comprehension lists , will help us in creating more cleaner logic and wite more efficient code in python. 