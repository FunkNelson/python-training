# if divisible by 3, print "Fizz"
# if divisible by 5, print "Buzz"
# if divisible by both 3 and 5, print "FizzBuzz"
# if not divisible by either, print the number

def fizz_buzz(input):
    answer = ""
    if input % 3 == 0:
        answer += "Fizz"
    if input % 5 == 0:
        answer += "Buzz"

    if answer:
        return answer
    else:
        return input


print(fizz_buzz(12))
print(fizz_buzz(25))
print(fizz_buzz(30))
print(fizz_buzz(7))
print(fizz_buzz(15))
print(fizz_buzz(2))
print(fizz_buzz(234235232))
print(fizz_buzz(3333))
