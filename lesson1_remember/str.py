s = "cat"
s = s.upper()
print(s)

s1 = 'Hello'
s2 = "Hello"
s3 = """Line one
Line two"""
print(s1)
print(s2)
print(s3)
print(s1, s2, s3, sep="\n")

#len()
s1 = "Python"
#slicing срезы -> my_string[start:end:step]
print(s1[2:4])
text = "automation"
print(text[2:4])
print(text[:4]) #если первой цифры нет то считает первые 4 цифры
print(text[4:]) #если есть только первая цифра то выдает все буквы кроме первых 4
print(text[::2]) #если не указана ни первая ни последняя строка последняя цифра показывает выдать каждую 2 букву
print(text[::-1]) #шаг -1 разворачивает строку
print(text[5:100])

name = "Mariia"
last_name = "Ivanova"
print(name + "" + last_name)
age = 25
print(name + "" + last_name + " - " + str(age))
print(f"Hi my name is {name} and my last name is {last_name} and my age is {age}")

#upper()/lower()
raw = "Automation QA"
print(raw.upper()) #поднимает буквы заглавные
print(raw.lower()) #опускает буквы маленькие

#strip()
print(raw.strip().upper())

#split() разрезает строку на отдельные части
#join() складывает строку

cvs_line = "Login, Cart, Checkout, Mama, Papa"
parts = cvs_line.split(",")
print(parts)
print(" - ".join(parts))

#replace() возвращает новую строку
msg = "Test failed: element not found"
print(msg.replace("failed", "passed"))

#find() возвращает -1 если подстрока не найдена
#index() возвращает ошибку если подстрока не найдена

s = "banana"
print(s.find("na"))
print(s.index("na"))

print(s.find("xyz"))
#print(s.index("xyz"))

#count() считает сколько в строке подстрок
print(s.count("na"))


