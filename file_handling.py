# file handling is a part of language , it provides built in functions and methods to read from and rite to files , both text and binary files. 


# read a whole file.

with open('sample.txt' ,'r' ) as file:
    content = file.read()
    print(content)
    
    
    
# read a file line by line
with open('sample.txt' , 'r') as file:
    for line in file:
        print(line.strip())
        
        
# overrirting 
with open('sample.txt', 'w') as file:
    file.write('Helloo')
    file.write("hey there is new file added , using write mode.")




# if we dont wanna overrerite 


# weshould open file in append mode, if we dont want to , the writing to get over write in same file. so use append while writing in file

with open('example.txt', 'a') as file:
    file.write("append option taking place")
    
    
# writing a list of lines in a file.

lines = ['first line \n', 'second line \n', 'third line \n', 'fourth line \n']

with open('example.txt', 'a') as file:
    file.writelines(lines)
    
    
# how to work with binary files.
data =  b'\x00\x01\x03'
with open('example.bin', 'wb') as file : 
    file.write(data)
    

# practical examples.




# to read  a text file adn count the number of lines , words and characters.

# def count_text_file(file_path):
#     with open(file_path, 'r') as file :
#         lines= file.readlines()
#         line_count = len(lines)
#         word_count = sum(len(line.split()) for line in lines)
#         char_count = sum(len(len) for line in lines)
#     return line_count , word_count, char_count



# file_path = 'example.txt'
# lines, words, characters  =count_text_file(file_path)

# print(f'lines : {lines}, words: {words} , characters: {characters}')


# Creating a new direcotry
import os
# new_directory = "package"
# os.mkdir(new_directory)
# print(f"direcotry '{new_directory}' created")

items= os.listdir('.')
print(items)

# joiing path , tihs is most important feature 

# dir_name = 'folder'
# file_name = "file.txt"
# full_path= os.path.join(car= {
#     'brand' : 'ford',
#     "model" : 'mustang',
#     "year": 1964
# }
# car.clear()
# print()                        
                        
                        
                        
                        
                        
                        
