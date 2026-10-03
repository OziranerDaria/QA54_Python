
#def clean_name(name):
    #return name.strip().title()

#print(clean_name("   anna smith   "))

def clean_name(name):
    a = name.strip()
    b = a.title()
    return b

print(clean_name("   anna smith   "))


def normalize_email(email):
    a = email.strip()
    b = a.lower()
    return b
print(normalize_email("  Anna.Smith@Example.COM  "))

def is_python_file(filename):
    a = filename.lower()
    b = a.endswith(".py")
    return b
print(is_python_file("lesson.py"))
print(is_python_file("HOMEWORK.PY"))
print(is_python_file("notes.txt"))


def fix_message(message):
    a = message.replace("bad", "good")
    return a

message = "bad weather, bad mood"
result = fix_message(message)
print(result)
print(message)


def count_letter(text, letter):
    a = text.lower()
    b = letter.lower()
    c = a.count(b)

    return c
print(count_letter("Programming", "g"))
print(count_letter("Mississippi", "I"))


def create_login(first_name, last_name):
    a = first_name.strip()
    b = last_name.strip()
    c = a.lower()
    d = b.lower()
#    return c + "." + d
    return f"{c}.{d}"
print(create_login("  Anna ", " SMITH  "))

