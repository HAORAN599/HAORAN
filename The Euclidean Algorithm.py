def GCD(A,B):  #use def to encapsulated code
    C = A % B  #define C,to caculate remainder
    if B == 0:  
       return A  #if B == 0,means the greast common divisor is A
    else:
       GCD(B, C)  #if not,continue to caculate, when B == 0,program stop
       