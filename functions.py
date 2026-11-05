# Functions are the block of codes that are used to perform a partcular tasks and return value. it is ussed bcoz it makes the code more readable easy to code.

# functions
def calculate(exp):
    total = 0
    for item in exp:
        total = total+item
    return total    


# to declare a function and make it, def keywoord is used.

exp_list = [2100,3400,3500]

joe_list = [200,400,500]

total = 0
for item in exp_list:
    total = total + item

print(total)

final = calculate(exp_list)
print(final)


for item in joe_list:
    total = total+item;

print(total);

def sum(a,b):
    """
    
    """
    total = a+b
    return total

n = sum(5,6)
print(n)
print(total)
