# Map function map() ,, applies a given function to all the items in a list , or any oter interable , can be dict tuple etc ,AND It returns a map object , (an iterator) , this is particularly useful for transforming data in a list comprehensively/


def square(num):
    return num **2 

print(square(4))

numbers = [3,2,4,56,4,4,4,3,2]

print(list(map(square , numbers)))



# using lambda function with map 
# lambda is when we have only one ligic with multiole arguments.

numbers1 = [ 3,21,43,5,3,3,2,2,3,4,4]
print(list(map(lambda x : x **2, numbers1 )))


# can we map multiple iterables 

numbers2 = [1,2,3]
numbers3 = [4,5,6]

added_num = list(map(lambda x , y: x+y , numbers2 , numbers3))
print(added_num)

# map() to convert list of string  to integerss.


str_num = ['23' , '233' , '4332', '5453']
int_num = list(map(int , str_num))

print(int_num)


words= ['apple', 'banana' , 'ccherry']
upper_word = list(map(str.upper , words))
print(upper_word)

# map function list of dictionary

def get_name(person):
    return person['name']

people =[
    {'name': "sakshi"  , "age" : 23} , 
    {'name' : 'jack' , 'age': 33}
]

print(list(map(get_name, people)))



