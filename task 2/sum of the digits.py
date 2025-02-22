def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total
number = 12345
print(f"The sum of the digits of {number} is {sum_of_digits(number)}.")
