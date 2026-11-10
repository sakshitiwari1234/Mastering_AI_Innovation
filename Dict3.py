# in this video we will learn about dictionary comprehension


# Dictionary comprehension is a concise way to create dictionaries.

squares = {x: x**2 for x in range(6)}
print(squares)

for i in range(10):
    print(f"{i} : {i*2}")
    

# practise practical examples of dictionary comprehension.

# use a dictionary to count the frequency of elemtns in list. 

numbers = [1,2 , 2,3,3,4,4,4,4]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number] =1
print(frequency)



# Merge two dictionaries into 1.

dict1 ={"a":1, "b":2}
dict2 = {"b":3, "c":4}

merges = {**dict1 , **dict2}

# need to learn keyword argument , and positional arguments.

