def leapyear_checker(year) -> bool:
    is_leap = False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            is_leap = False
        is_leap = True

    return is_leap


print(leapyear_checker(2020))
print(leapyear_checker(2025))
