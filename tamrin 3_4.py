def find_pairs(postal_codes, target_sum):
    postal_code_dict = {code: i for i, code in enumerate(postal_codes)}
    pairs = []
    for i, code in enumerate(postal_codes):
        diff = target_sum - code
        if diff in postal_code_dict and i < postal_code_dict[diff]:
            pairs.append((i, postal_code_dict[diff]))
            del postal_code_dict[diff]
    return pairs

def print_pairs(pairs):
    if not pairs:
        print("Not Found!")
    else:
        pairs.sort(key=lambda x: x[0] + x[1])
        for pair in pairs:
            print(pair[0] + pair[1])

postal_codes = list(map(int, input().split()))
target_sum = int(input())
pairs = find_pairs(postal_codes, target_sum)
print_pairs(pairs)
