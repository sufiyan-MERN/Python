list1 = [1,2,1,8]
copy_list= list1.copy()
copy_list.reverse()

if copy_list == list1:
    print("palidrome") 
else:
    print("not palindrom")


grade_tuple = ("A","B","C","A","D","A","C","D")
student_A = grade_tuple.count("A")
print(student_A)

grade_list = ["A","B","C","A","D","A","C","D"]
grade_list.sort()
print(grade_list)