
def print_list_reverse(lst):
    if lst is None:
        print("Wrong list")
    elif len(lst) == 0:
        print("Wrong list")
    elif type(lst) != list:
        print("Wrong type")
    else:
        lst.reverse()
        print(lst)
print_list_reverse(None)
print_list_reverse([])
print_list_reverse("ghj")
print_list_reverse([1, 2, 3, 4, 5])


def is_valid_point(point):
    if point is None:
        return None
    elif point == ():
        return None
    elif not isinstance(point, tuple):
        return False
    elif len(point) != 2:
        return False
    elif not isinstance(point[0], (int, float)):
        return False
    elif not isinstance(point[1], (int, float)):
        return False
    else:
        return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))





def print_sublist_reverse(lst, start, finish):
    if lst is None:
        print("Wrong args")
    elif not isinstance(lst, list):
        print("Wrong args")
    elif len(lst) == 0:
        print("Wrong args")
    elif not isinstance(start, int):
        print("Wrong args")
    elif not isinstance(finish, int):
        print("Wrong args")
    elif start >= len(lst):
        print("Wrong args")
    elif start < 0:
        print("Wrong args")
    elif finish >= len(lst):
        print("Wrong args")
    elif finish < 0:
        print("Wrong args")
    elif start > finish:
        print("Wrong args")
    else:
        part = lst[start:finish + 1]
        part.reverse()
        lst[start:finish + 1] = part
        print(lst)
print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([1, 2, 3], "0", 2)



def get_students_by_grade(students):
    if students is None:
        return {}
    elif not isinstance(students, dict): #класс дикт
        return {}
    elif len(students) == 0:
        return {}
    result = {}
    for name, grade in students.items():
        if grade in result:
            result[grade].append(name)
        else:
            result[grade] = [name]
    return result
print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))
print(get_students_by_grade(None))

