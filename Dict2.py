# Iterating in dictionaries 

# In this module we will learn how to iterate in dictionaries.

# we can use loops in dictionaries to iterate through the keys and values of the dictionary.
# items is combination of key and value both.

# Iterating over keys of dictionary.

Student4 = {"name" : "Parul" , "age" : 25, "course" : "python" , "address" : "delhi"}

# now if i have to iterate voer keys.
for i in Student4.keys():
    print(i)


for i in Student4.values():
    print(i)



for i in Student4.items():
    print(i)
    
    
for key,value in Student4.items():
    print(f"{key}: {value}")
    
# Nested dictionary:

students= {
    "student1" : {"name" : "Parul" , "age" : 25, "course" : "python" , "address" : "delhi"}, 
    "Student2": {"name" : "Aditya" , "age" : 19, "course" : "python" , "address" : "delhi"},
    "Student3": {"name" : "Rahul" , "age" : 20, "course" : "python" , "address" : "mumbai"}
    
}

print(students)

# how toa ccess the elements of nested dictionary.
print(students["student1"]["name"])

print(students["Student2"]["age"])
print(students["Student3"]["address"])


# we can create our own nested dictionary as well. and play with them accessing any way we want.

# Now how to iterate over nested dictionary.

for i , j in students.items():
    print(f"{i}:{j}")
    

