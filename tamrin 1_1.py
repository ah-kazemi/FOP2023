a = int(input())
b = int(input())

if (0 <= a <= 2 ** 30) & (0 <= b <= 2 ** 30):
    result = bin(a ^ b).count("1")
    print(result)