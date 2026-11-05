# building the applicatiion project , we studeid about list in previous lecture , we studied about lists and comprehension , in this video we will study what application , ususes the practical way of using lists.

#  building a study to do list. 


to_do_list = ["buy groceries" , "clean the house" , "paybills"]

# i have to do more task to add in list. i can add directly right?
to_do_list.append("study python")

to_do_list.append("to go for a run")
to_do_list.append("workout")

# Now i did some task and wanna remove those task , what i can directly use 

to_do_list.remove("paybills")

# Wanna check if gets remove , add or not.

if "paybills" in to_do_list:
    print("do not forget to pay the bills . reminder well")
    

print("Remained to do list")
for task in to_do_list:
    print(f"-{task}")
    


# ORGANIZING STUDENT GRADES
grades = [85, 92 , 78 , 90 , 88]

# adding a new graade - 

grades.append(100)

# calculating the average grade
average_grade = sum(grades) / len(grades)
print(f"Average grade : {average_grade: .2f}")


# finding highest and lowest grades
highest_grade = max(grades)
lowest_grades = min(grades)


# Managing an inventory

# use a list to manage inventory items in a store


# managin an inventory
inventory = ["apples" , "bananas" , "oranges", "grapes"]

# adding a new item
inventory.append("strwaberries")

inventory.remove("bananas")

item = "oranges"
if item in inventory:
    print(f"{item} are in stock")
else:
    print(f"{item} are out of stock" )
    
    
print(f"the entire inventory is this - {inventory}")



# Collect the user feedback , in form of a list.
# collect the user feeedback


