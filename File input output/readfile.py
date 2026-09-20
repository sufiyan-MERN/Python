f = open("demo.txt")
data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)


f = open("demo.txt","w")
data = f.write("i am learning python")
print("data saved sucessfull")

f = open('demo.txt',"a")
data = f.write("\n after that springBoot")


f = open("sample.txt","w")
data = f.write("this file is created using file input and output methods")