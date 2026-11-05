# we willl study about dictionaries in this.

# 1. introduction to doctionaries
# 2. creating dictionaries. 
# 3. accessign dcitionaries.
# 4. modifying dictionaries.
# 5. Dictionary method
# 6. iterating over dictionaries.
# 7. nested dictionaries
# 8. dictionary comprehension.
# 9. Dictionary practical examples and common errors. 

# Dictionaries are used to store data value in key value pairs. it is unordered collection of items. key must be uniqye and it should be immutable. key cannot be change at all. for example: strings, numbers, or tuples. in which values can be of any type.

# Creating dictionaries.

empty_dict = {}
print(type(empty_dict))

empty_dict = dict()
print(empty_dict)

# initlizing a dictionary with some values.

student = {"name" : "rajai" , "age" : 20 , "course" : "python"}
print(student)


# Error
student = {"name" : "rajai" , "age" : 20 , "course" : "python" , "name" : 24}
print(student)

# if i againd define the  , key with same key and different value, it will take the last value and it will override the previous value.


student = {"name": "krish" , "age": 23}
print(student)

