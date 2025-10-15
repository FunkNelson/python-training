def fibonacci_maker(size):
    print("Fibonacci sequence:")

    current_number = 0
    last_number = 1
    two_numbers_ago = 0
    print("0 1", end=" ")

    while size > 2:
        current_number = two_numbers_ago + last_number
        print(f"{current_number}", end=" ")
        two_numbers_ago = last_number
        last_number = current_number
        size -= 1

    print(" ")


fibonacci_maker(15)
