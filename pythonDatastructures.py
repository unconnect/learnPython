from pythonControlFlow import divider
from pythonControlFlow import fac
from collections import deque


# List Operations
def print_my_lists():
    my_list = []
    my_list.extend((1, 2, 3, 4))
    my_list.insert(2, 2.5)
    i = len(my_list)
    n = i
    while i > 0:
        my_list.append(n)
        i = i - 1
        n = n + 1
    my_list.append(2)
    my_list.sort()

    divider()
    print('Lists:')
    print(my_list)
    print(my_list.count(2))

    my_list = deque(my_list)
    my_list.append('The One')
    my_list.append('The Two')
    print(my_list)
    my_list.popleft()
    print(my_list)

    faculties = []
    for x in range(1,8):
        faculties.append(fac(x))

    # This is the equivalent to build faculties
    faculties2 = [fac(x) for x in range(1,10)]

    print(faculties)
    print(faculties2)