# def calcu_sum(a,b):
#     sum = a+b 
#     print(sum)
#     return sum

# calcu_sum(2,10)
# calcu_sum(6,1)
# calcu_sum(39840,982309)

# def calcu_sum(a,b):
#     return a+b
# sum = calcu_sum(4,5)
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# #average of three numbers

# def avg_three(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg
# avg_three(94,95,92)

# cities = ["delhi","hyderabad","mumbai","pune"]
# heroes = ["thor","ironamn"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

# def print_list(list):
#     for item in list:
#         print(item,end=" ")

# print_list(cities)
# print_list(heroes)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)

factorial(10)

def converter(usd_value):
    inr_val = usd_value * 83
    print(usd_value,"USD =",inr_val,"INR")

converter(48)

def odd_even(number):
    if(number ==0):
        print("number is 0")
    elif(number %2 == 0):
        print("EVEn")
    else:
        print("odd")

odd_even(7)