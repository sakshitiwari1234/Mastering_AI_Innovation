# lambda functions are small anonymous functions defined uisng the lambda keyword. they can have any number of arguments but only one expression that means only one , logic to be implementted using those arguments. they are used for shorr operations or as arguments to higher order functions. 

# Syntax

# lambda arguments : expression

# how does this work ?

# def addition(a,b):
#     return a+b


# print(addition(24,34))

# lambda is func without name

addition = lambda a,b : a+b
type(addition)

print(addition(342,42))

# def even(num):
#     if num%2 ==0:
#         return True
    
# even(24)


even1 = lambda num : num%2==0
print(even1(5345))


def addition(x,y,z):
    return x+y+z

print(addition(4,2,5))




addition1 = lambda x,y,z : x+y+z
print(addition1(243,453,432))



# It has some more features. such as map and filter feture . 

# Map() function

numbers = [ 32 ,2,1,3,4,3]

def square(numbers):
    return numbers **2 

print(square(2))   # here i have make a list and made some function to make the square of a number passed. but it is only performing for 1 input. what if i want to pass multiple arguments to get the operation perform. or what if i want the operation to get done on each of this list , then map function is quite useful. it can be used to apply a function to all items in a list. 


# Syntax for map - 
#  map has two arguments
# map(function , **iterables)
print(list(map(lambda x : x**2 , numbers )))




