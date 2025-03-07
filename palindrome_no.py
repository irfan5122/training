n = int(input())
original_number = n
rev = 0


while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10


if original_number == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
