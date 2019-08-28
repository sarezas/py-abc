# print("Hello, World!")

# first = 9
# second = first + 1


# def add(a, b):
#     print(a + b)


# add(first, second)

# """asdsdsd"""

# cars = ["audi", "mercedes-benz", "bmw", "volkswagen", "volvo", "seat"]
# name = "Sharis"
# dumb = False

# if name:
#     print(name)


# if name == "Sharis" and not dumb:
#     cars.append("opel")
#     print(cars[:1])


# a = 9
# b = 10

# "bigger" if b > a else "smaller"

# for car in cars:
#     print("The cars in the list include {0}".format(car))


# x = 0
# for index in range(10):
#     x += 10
#     print("The value of x is {0}".format(x))


# students = ["Antanas", "Petras", "Stasys", "Mindaugas", "Elze",
#             "Jurgita", "Sarunas", "Ilona", "Virginija", "Nijole", "Egle", "Pranas"]

# for student in students:
#     if student == "Sarunas":
#         print("Found him - " + student)
#         continue
#     print("Searching for the match: " + student + " going to next")


# phrase = "Sharis is cool"

# for char in phrase:
#     print(char)


# student = {
#     "name": "sharis",
#     "last_name": "maris",
#     "id": 19,
#     "attendance": "excellent"
# }


# try:
#     x = student["grades"]
# except KeyError as error:
#     print("This key is not found!")
#     print(error)

# print("This code still executes")

friends = []


def get_friends_titlecase():
    friends_titlecase = []
    for friend in friends:
        friends_titlecase.append(friend["name"].title())

    return friends_titlecase


def print_friends_titlecase():
    friends_titlecase = get_friends_titlecase()
    print(friends_titlecase)


def add_friend(name, id=19):
    friend = {"name": name, "id": id}
    friends.append(friend)


def save_file(friend):
    try:
        f = open("friends.txt", "a")
        f.write(friend + "\n")
        f.close()
    except Exception:
        print("Could not save to file")


def read_file():
    try:
        f = open("friends.txt", "r")
        # itterate through a function generator
        for friend in read_friends(f):
            add_friend(friend)
        f.close()
    except Exception:
        print("Could not read file")


def read_friends(file):
    for line in file:
        yield line


# lambda functions
def double(x): print(x * 2)


def tripple(y): print(y * 3)


read_file()
print_friends_titlecase()

friend_name = input("Enter friend name: ")
friend_id = int(input("Enter friend ID: "))

add_friend(friend_name, friend_id)
save_file(friend_name)
read_file()
double(19)
tripple(5)

#list comprehension
numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#print a new list of numbers which are less than 5 from the given numbers list in one line
print([number for number in numbers_list if number < 5])
#print([[output] [itteration] [condition]])

# => [1, 1, 2, 3]

#give divisors of a particular number from user input

def show_divisors(number_from_input):
    number_range = list(range(1, 1001))
    for nr in number_range:
        if nr % number_from_input == 0:
            print(nr)
                
                
nr_from_input = int(input("Give me a number: "))
show_divisors(nr_from_input)

#given two lists print out a new list only of common items in both lists without duplicates

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def find_in_lists(list1, list2):
    common_numbers = []
    for number in list1:
        if number in list2:
            if number not in common_numbers:
                common_numbers.append(number)
                print(common_numbers)
            
                
find_in_lists(a, b) 

#do the same in one line and add list c before it
c = []
print([number for number in b if number in a and number not in c])
