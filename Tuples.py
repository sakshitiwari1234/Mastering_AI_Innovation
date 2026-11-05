# Tuples

# Intorduction , creating tuples,  immutable tuples nature , tuple methods , nested tuples etc.

# Tuples are ordered collection of items , and they are immutable in nature. 

# So tuples are , ordered in nature , they are immutable in types and created using parenthesis.

# creating a tuple.
empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))


lst = list()
print(type(lst))

tpl = tuple()
print(type(tpl))


# adding elements in tuple.

numbers = tuple([1,2,3,4,5,6,7])
print(numbers)

list((1,2,3,4,5,67,7))
print(list)


# all kind of data can be given or inserrtd in tuple.

mix_tpl = (1, "hello" , True)
print(mix_tpl)


# accessing tuple elements.

print(numbers[2])

tpll = (1,2,3,4, "car" , "rajai" , "baarish" , )

print(tpll)

print(tpll[:: -1])

# tuples operations. it supports various operations. 


tpll * 3

print(tpll)

numbers * 2
print(numbers)


# immutable nature of tuples

# tuple cannot be changed at all. they cannot be change once elments are assign.

lstt = [1,2,3,4,5]
print(lstt)

lstt[2]= ["sakshi"]
print(lstt)

lstt[2] = "aditya"
print(lstt)


# tuple methods
print(numbers.count(4))

# print(numbers.index(3))  in which index is a function, which returns the first index of the value that is on which index this number occurs. these are common methods used in tuple 

# PACKING AND UNPAKCING TUPLE.

packed_tuple = 1, "hello" , 3.14

print(packed_tuple)

# packing and unpakcing means converting the entire elemetns into tuple form.

# unpacking a tuple happens in this way.

a,b,c = packed_tuple
print(b)
print(c)
print(a)



# unpacking with a *

numbers = (1,2,3,4,5,6,7,8,9)
first, *middle, last = numbers

print(first)    # what does last elemetns does , it prints all the elemtns that are present , in between the first and last elements.

print(middle)
print(last)

# Till the last element , all elements will be picked up. 

# Nested tuples.

lst= [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15,16], [17,18,19, "c"]]


lst[0]

print(lst)
print(lst[1][3])

# i want to use slicing operations.
lst[0][0:3]


nested_tuple = ((1,2,3),("a" , "b" , "c") , (True, False))

# Access the elements

print(nested_tuple[0])
print(nested_tuple[1][2])


# iterating over a nested tuples.

for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item ,  end = " ")
    print()
    
    
