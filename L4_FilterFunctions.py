# The filter functions in python. The filter function is python are the functions that consturctors an iterator from elements of an iterable for which a ducntion returns true. it is used to filter out items , from a list or any other interable , based on a condition.


# used to filter items in a list.

def even(num):
    if num%2 == 0:
        return True
    
# what if we have  lsit of itmes and the we want to know how many elements are actually even or not , in this case we use filter function by iterating 

lst = [1,34,5,66, 2,2,3,5,6,7,7,5,4,3,2,2]

final = list(((filter(even , lst))))

print(final)



# Fiter with lambda function 
numbers = [1,2,3,4,5,5,3  ,34,243,34]
greater =  list(filter(lambda x : x > 5 , numbers))
print(greater)

# Filter with lambda fnunction and mutiple conditons

nmbr = [1,2,3,4,5,3,6,65,4]
even_and_greater = list(filter(lambda x:x>5 and x%2==0 , nmbr))
print(even_and_greater)

