    # def main():
    #     name = get_name()
    #     houre = get_house()
    #     print(f"{name} from {houre}")

    # def get_name():
    #     return input("Name: ")

    # def get_house():
    #     return input("House: ")

    # def main():
    #     name, house = get_student()
    #     print(f"{name} from {house}")

    # def get_student():
    #     name= input("Name: ")
    #     house= input("House: ")
    #     return name, house

def main():
    student = get_student()
    if student[0] == "ZIMS":
        student[1] = "Tolla"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name= input("Name: ")
    house= input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()