def sum_of_divisors(a):
    return sum(i for i in range(1, a+1) if a % i == 0)


def convert_to_base(num, base):
    if base < 2 or base > 9:
        print("invalid base!")
        exit(0)
    digits = []
    while num > 0:
        remainder = num % base
        digits.append(remainder)
        num //= base
    digits.reverse()
    return int(''.join(map(str, digits)))


def calculate_sum_and_convert(n, b):
    sum = sum_of_divisors(n)
    return convert_to_base(sum, b)

converted_numbers = []
while True:
    n, b = map(int, input().split())
    if n == -1 and b == -1:
        break
    converted_numbers.append(calculate_sum_and_convert(n, b))

print(sum(converted_numbers))
