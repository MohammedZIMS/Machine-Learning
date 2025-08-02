def main():
    name = get_name()
    houre = get_house()
    print(f"{name} from {houre}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()