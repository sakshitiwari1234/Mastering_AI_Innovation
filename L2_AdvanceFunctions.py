# in this video we will study aabout advance functions and some examples 

def convert_temp(temp, unit):
    """this funcion converts temp between celcius and farenheit."""
    if unit =='C':
        return temp * 9/5 + 32  #farehnehti me hoga convert
    elif unit == "F":
        return (temp-32) * 5/9
    else:
        return None
    
print(convert_temp(25,'C'))

    
print(convert_temp(34,'F'))
    
    
# Example 2 --> Password Strength checker. 


def is_strong_password(password):
    """this password checks if the password is strong or not"""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()' for char in password):
        return False
    return True



# calling the functions 
print(is_strong_password("sakshi#020333"))




# to calculate the total cost of items in cart

# def calculate(cost):
#     total_cost = 0
#     for item in cart:
#         total_cost = total_cost + item['cost']* ['quant']


# # some exampeles for data

# cart = [
#     {'name' : 'apple' , 'price':0.5, 'quant': 234} , 
#     {'name': 'Banana', 'price:': 4 ,' quant': 23}
    
# ]


    
# results = calculate(cart)
# print(results)
    
    

    
# to check whether a string is palindrome or not

def pal(s):
   s = s.lower().replace(" " ,"")
   return s == s[::-1]


# pal("sakshi")
# pal("abba")..


# factorial of a numbr using recursion. 

def fact(n):
    if n== 0:
        return 1
    else:
        return n *  fact(n-1)
    
print(fact(5))
    
    
# A function to read a file and count the frequency of , each word

# def freq(file_path):
#     word_count={}
#     with open(file_path, 'r') as file:
#      for line in file:
#         words= line.split()
#         for words in word:
#             word = word.lower().strip('.,!?;:"\'')
#             word_count[word]= word_count.get(word,0)+1
            
#     return word_count



# filepath = 'sample.txt'
# result = freq(filepath)
# print(result)
            
                                      
            
        
    
# to validate email address of a person

import re

# email validation fn
def is_valid(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern,email) is not True


print(is_valid("test@example.com"))


