# what are functions , 
# defining function
# calling fucntions 
# default functions
# function parameters
# parameter defualt
# variable length arguments 
# return statemenrs 


#  ehy do we require functions  . we know 

num = 24
if num%2 ==0:
    print("number is even")
else:
    print("odd")
    
    
# i can write this entire code inside function

def evenodd(num):
    """this function finds even or odd"""
    if num%2 == 0 :
        print("even no")
    else:
        print("the number is odd")
        


# call this function , 
evenodd(35)

# to call any function we can simply , write the name of the fn , and pass the paraemter , inside parentrsis , calling a function dont require to build a , main function at all. 

# function with multiple parameters

def add(a , b):
    return a +b;


print(add(23434,24234));


result = add(2344,4243);
print(result)



# default paramters , are the paramter that are are actually set by default without giving

def greet(name = "guest"):
    print(f"Hello {name} welcome to the home ")
    
    
    
    
greet("krish")


greet()


# Variable length arguments. 

# positional and keyword arguments. 

# positional arguments can have multiple number of arguments. 
def print_numbers(*args): #this is postional argument
    for numbers in args:
        print(numbers)
        
        
        
print_numbers(1,2,3,4,4,5,4,"sakshi")

# keyword arguments


#  all the arguments , in this ketword arguments are in form of key value pairs
def print_Details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
    

print_Details(name= "sakshi" , age= 23 , address = "agyaram colony")



# we can use both positional argument and keyword argument together too

def drive(*args , **kwargs):
    for numbers in args:
        print(numbers)
        
    for key,value in kwargs.items():
        print(f"the feature value is this: {key} , and value is this : {value}")
        
        
        
drive(2,3,5,3,2,5,33 , name = "sakshi" )


# return statements return the multiple parameters. 
