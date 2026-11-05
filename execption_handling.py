# exception handling are the erros or problems that may occur while we are executing some , our programs.

x = input("enter number")
y = input("enter number 2")
try:
     z  = int(x)/ int(y)
except Exception as e:
     print('exeption occured:', e)
     z= None

except Exception as e:
     print('exception type:', type(e).__name__)  # important this is very much.   
print("division is:", z)     
         
print("division isL", z)

# how to handle multiple exeptions.

