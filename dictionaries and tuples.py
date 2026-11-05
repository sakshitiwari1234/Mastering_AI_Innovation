dict ={"sakshi": 4323342424, "unknown": 3243244323, "palak": 325456535, "tanu": 3432432}

print(dict["sakshi"])

# here we retrive the value in dictionaryy by any key.

dict["oshank"] = 545464

print(dict)


# to delete any pair from dictionary

del dict["unknown"]
print(dict)


for i in dict:
    print("key", i , "value" , dict[i])

# to check whether pair is present in dictinary or not.

# we use ***in** operator.

print("oshank" in dict)

dict.clear()
print(dict)



# TUPLES IN PYTHON 

# tuple is a group of values that is grouped together.

sakshi = (23,43,23,123,32,323,242,123,12342,3434,4,34435,34543,32,432)
print(sakshi)

sakshi[3]
print(sakshi[3])

# tuples are immutable in nature.

# INRODUCTION TO MODULES

# MODULES  are the already made written code writtten already by someone so taht our code become easy to use , and ready to use for freee of cost

import math
print(math.sqrt(44))

print(math.pow(3,2))

print(math.pi)
print(math.log10(100))

print(math.floor(2.343))

import calendar

cal = calendar.month(2024,1)
print(cal)

import functions
area = functions.exp_list
print(area)