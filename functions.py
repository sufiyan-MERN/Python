def calcu_sum(a,b):
    sum = a+b 
    print(sum)
    return sum

calcu_sum(2,10)
calcu_sum(6,1)
calcu_sum(39840,982309)

def calcu_sum(a,b):
    return a+b
sum = calcu_sum(4,5)
print(sum)

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

#average of three numbers

def avg_three(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
avg_three(94,95,92)

cities = ["delhi","hyderabad","mumbai","pune"]
heroes = ["thor","ironamn"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)
print_list(heroes)