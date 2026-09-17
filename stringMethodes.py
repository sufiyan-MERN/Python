name = "python full stack developer"
text = "Developement"

print(name.capitalize())
print(name.count(name))

email = "    sufiyantdc@gmail.com   "
print(email.strip())

sentence = "python,java,c++,javascript"
languages = sentence.split(",")
print(languages)

words = ["learn","python","for","AI/ML"]
join = " ".join(words)
print(join)


sentence = "i love coding in java"
new_text = sentence.replace("java","python")
print(new_text)
print(new_text.find("python"))
print(new_text.lower().count("coding"))


text = "PythON ProGRAmmINg"
print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())