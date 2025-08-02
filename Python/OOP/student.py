    # def main():
    #     name = get_name()
    #     houre = get_house()
    #     print(f"{name} from {houre}")

    # def get_name():
    #     return input("Name: ")

    # def get_house():
    #     return input("House: ")

# Tuple
    # def main():
    #     name, house = get_student()
    #     print(f"{name} from {house}")

    # def get_student():
    #     name= input("Name: ")
    #     house= input("House: ")
    #     return name, house

# Tuple wit List
    # def main():
    #     student = get_student()
    #     if student[0] == "ZIMS":
    #         student[1] = "Tolla"
    #     print(f"{student[0]} from {student[1]}")

    # def get_student():
    #     name= input("Name: ")
    #     house= input("House: ")
    #     return [name, house]

# Dictionary.
    # def main():
    #     student = get_student()
    #     if student["name"] == "ZIMS":
    #         student["house"] = "Tolla"
    #     print(f"{student['name']} from {student['house']}")


    # def get_student():
    #     name = input("Name: ")
    #     house = input("House: ")
    #     return {"name": name, "house": house}

class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()