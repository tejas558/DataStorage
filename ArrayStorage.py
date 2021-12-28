storage = []

while True:
    print("type i to insert")
    print("type f to find")
    print("type d to delete")
    print("type p to print all")
    print()
    x = input('Input your operation: ')
    if x == 'i':
        val = input('type the value that you want to insert: ')
        if val in storage:
            print("this value already exists in storage")
        else:
            storage.append(val)
            print("this value has been added to storage")
    elif x == 'f':
        val = input('type the value taht you wish to find')
        if val in storage:
            print('this value has been found')
        else:
            print("this value was not found in storage")
    elif x == 'd':
        val = input("type the value that you would like to delete")
        if val not in storage:
            print("failed to delete", val, "this value was not in storage")
        else:
            storage.remove(val)
    elif x == 'p':
        print(storage)
    else:
        break