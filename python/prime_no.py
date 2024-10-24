def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime numbers up to 100:")
for number in range(2, 101):
    if is_prime(number):
        print(number, end=" ")

