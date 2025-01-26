A = int(input("please enter the first integer number "))  #asking user enters two integers
B = int(input("please enter the second integer number "))

def GCD(A,B):  #use def to encapsulated code
    if B == 0:  
       return A  #if B == 0,means the greast common divisor is A   
    else:
       return GCD(B, A % B)  #if not,continue to caculate, when B == 0,program stop

while  A < 0 or B < 0:  #To check does user enter the integer number,if not,try again
    print("the number must greater than or equal to 0,please try again")  
    A = int(input("please enter the first number "))  #Reenter to numbers
    B = int(input("please enter the second number "))
    
print("the Greatest Common Divisor between",A,"and",B,"is",GCD(A, B))  #if 2 number >= 0,calculate the greatest common number



       