while True:
    user_input = input()

    calculation = user_input[::-1]
    if user_input == '0':
        break

    if user_input == calculation:
        print('yes')

    elif user_input != calculation:
        print("no")

