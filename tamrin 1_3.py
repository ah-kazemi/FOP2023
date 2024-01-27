a ,b =map(int, input().split())
if (0 <= a) & (a <= 1000) & (0 <= b) & (b <= 1000) :
    if a > b :
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True


        def count_prime_numbers(start, end):
            count = 0
            for num in range(start, end + 1):
                if is_prime(num):
                    count += 1
            return count

        prime_count = count_prime_numbers(b, a)
        print ("reverse order - amount: " + str(prime_count))

    else :
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True


        def count_prime_numbers(start, end):
            count = 0
            for num in range(start, end + 1):
                if is_prime(num):
                    count += 1
            return count

        prime_count = count_prime_numbers(a, b)
        print("main order - amount: " + str(prime_count))