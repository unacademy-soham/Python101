# # This code helps us decide whether we should go out
#
# def print_choice_message():
#     print("Select your choice.")
#     print("1. Add a record")
#     print("2. Update a record")
#     print("3. Get a record")
#     print("4. Exit")
#
#
# def get_student_details():
#     print("Enter student name: ", end=" ")
#     name = input()
#     print("Enter student marks: ", end=" ")
#     marks = int(input())
#
#     return name, marks
#
#
# print("--------- WELCOME TO UNACADEMY CLASSES. ------------")
#
# records = dict()
#
# while True:
#     print_choice_message()
#     choice = int(input())
#     if choice == 1 or choice == 2:
#         name, marks = get_student_details()
#         records[name] = marks
#     elif choice == 3:
#         print("Enter student name: ", end=" ")
#         name = input()
#         print("Marks is: ", records[name])
#     else:
#         break

#
# arr = list(map(int, input().split()))

"""
1/7/2021

01-07-2021
"""

def prettify_date_string(date_string):
    date_string = date_string.split("/")
    for i in range(len(date_string)):
        date_string[i] = date_string[i].zfill(2)
    return date_string[0] + "-" + date_string[1] + "-" + date_string[2]


print(prettify_date_string("1/7/2021"))
