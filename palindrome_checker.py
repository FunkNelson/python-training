given_number = 125521242342342


def palindrome_checker(number):
    number_string = str(number)
    number_length = len(number_string)
    is_palindromy = True

    start_index = 0
    end_index = -1

    while is_palindromy and start_index < number_length / 2:
        if number_string[start_index] == number_string[end_index]:
            start_index += 1
            end_index -= 1
        else:
            is_palindromy = False
            break

    return is_palindromy


print(given_number)

if palindrome_checker(given_number):
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")
