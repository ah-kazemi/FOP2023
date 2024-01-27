def calculate_trap(operation, numbers):
    if operation == "sum":
        return sum(numbers)
    elif operation == "average":
        return round(sum(numbers) / len(numbers), 2)
    elif operation == "lcd":
        def find_lcd(x, y):
            if x > y:
                greater = x
            else:
                greater = y
            while True:
                if greater % x == 0 and greater % y == 0:
                    return greater
                greater += 1

        result = numbers[0]
        for i in range(1, len(numbers)):
            result = find_lcd(result, numbers[i])
        return result
    elif operation == "gcd":
        def find_gcd(x, y):
            while(y):
                x, y = y, x % y
            return x

        result = numbers[0]
        for i in range(1, len(numbers)):
            result = find_gcd(result, numbers[i])
        return result
    elif operation == "min":
        return min(numbers)
    elif operation == "max":
        return max(numbers)

trap = input(str())
numbers = []

import sys
if trap not in ["sum", "average", "lcd", "gcd", "min", "max"]:
    print("Invalid command")
    sys.exit()

while True:
    line = input()
    if line == "end":
        break
    try:
        number = int(line)
        numbers.append(number)
    except ValueError:
        print("Invalid command")
        sys.exit()

print(calculate_trap(trap, numbers))
