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

# accessnig dictionary elements
student = {"name" : "rajai" , "age" : 20 , "course" : "python"}
print(student['course'])

# to access elements , put key in square brackets. if key is not present in dictionary, it will give key error.

# thisn is one of the easiest way

# we can also get the element using get method

print(student.get('name'))
print(student.get('course'))
print(student.get('last_name'))
# when i search for last name we get none because it is not present in the dictionary. but it will not give key error.

print(student.get('last_name', 'not found in the dictionary'))



# there are two methods to access the elements of dictionary. 1. using square brackets and 2. using get method.




# Modifying dictionary elements. 

# dictionary elements can be modified by using key name in square brackets. if key is present in the dictionary, it will update the value of that key. if key is not present in the dictionary, it will add that key value pair to the dictionary. 

# Dictionary are mutable , which means we can update ,a ddd , delete the elements of dictionary.

Student2 = {"name" : "Aditya" , "age" : 19, "course" : "python" , "address" : "delhi"}

# changin the age
Student2['age'] = 20
print(Student2)


# to delete key
Student2.pop('address')
print(Student2)


# using delete keyword
del Student2['course']
print(Student2)

# Important dictionary methods.

# to get all keys of dictionary we can use keys() method. it will return all the keys of dictionary in a list.

keys = Student2.keys()
print(keys)     
values= Student2.values()
print(values)


# I want to get key value pairs.

items = Student2.items() 
print(items)
#  using items method , we can get all the key value pairs , in form of tuples , like all elements are presented in form of key and values.


# I want to do a shallow copy of dictionary. we can use copy method to do that.

Student3  = Student2.copy()

print("this is student 3 details" , Student3)
Student3["name"] = "Sakshi"
print("this is student 3 details" , Student3)

# Shallow copy means if we change the value of student3, it will not affect the student2. because it is a shallow copy. but if we change the value of student2, it will not affect the student3. because it is a shallow copy.

print(Student2)



