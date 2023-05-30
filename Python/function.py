# def sm(a,b):
#     print(a+b)

# sum=sm(2,3)

# def even(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"
#     for i in range(1,10):
#         val=int(input("enter the number: "))
#         check=even(val)
#         if check=="even":
#             print("even")
#         else:
#             print("odd")

# WAP to return square of a number.

# def square(a):
#     # val=(a^2)
#     val=pow(a,2)
#     return val
# a=int(input("enter any number:"))
# val=square(a)
# print(val)


# def print_sq_rt(a):
#     val=(a**(1/2))
#     return val
# a=int(input("Enter any number: "))
# val=print_sq_rt(a)
# print(val)
    
def prime(a):
    for i in range(2,a):
        if a%i==0:
            return "not prime" 
        else:
            return "prime"   
    