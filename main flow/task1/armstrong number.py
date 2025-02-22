def is_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == n
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number!")
else:
    print(f"{number} is not an Armstrong number.")
