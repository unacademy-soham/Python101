import logging

logger = logging.getLogger("errorLogger")

class ErrorCatchingExample:
    def __init__(self):
        self.arr = [1, 2, 3, 4, 5]

    def get_value_for_index(self, index):
        if index < 0:
            raise AttributeError("Index is negative")

        if index >= len(self.arr):
            raise AttributeError("Index out of bounds")
        return self.arr[index]


e = ErrorCatchingExample()
while True:
    print("Enter choice")
    print("1. Enter a index")
    print("2. Exit")

    ch = int(input())

    if ch == 2:
        break

    else:
        try:
            index = int(input())
            print(e.get_value_for_index(index))
        except AttributeError as e:
           logger.error(e)
