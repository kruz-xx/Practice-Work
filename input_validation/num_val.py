while True:
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        print("Valid number:", number)
        break
    except ValueError:
        print("Invalid input. Try again.")
