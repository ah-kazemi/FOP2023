import re

class DNA:
    def __init__(self, dna):
        self.dna = dna

class Kharchang(DNA):
    def __init__(self, dna):
        super().__init__(dna)
        self.dna += self.dna[0:10]

    def mutate(self):
        return self.dna.replace('tt', 'o')

class Bob(Kharchang):
    def __init__(self, dna):
        super().__init__(dna)
        self.dna = int(''.join(map(str, self.merge_sort([int(d) for d in str(len(self.dna))]))))

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left if left else right)
        return merged



class Okhtapus(DNA):
    def __init__(self, dna):
        super().__init__(dna)
        self.dna = self.add_x_to_end()

    def replace_triples(self):
        triples = re.findall(r'(.)\1{2}', self.dna)
        for triple in triples:
            self.dna = self.dna.replace(triple*3, '(0_0)')
        return self.dna

    def add_x_to_end(self):
        x_index = self.linear_search('x')
        if x_index != -1:
            self.dna += str(x_index)
        return self.dna

    def linear_search(self, target):
        for i in range(len(self.dna)):
            if self.dna[i] == target:
                return i
        return -1

def validate_input(input):
    if input.startswith('m'):
        return Kharchang(input).mutate()
    elif input.startswith('sb'):
        return Bob(input).dna
    elif input.startswith('s') and not input.startswith('sb'):
        return Okhtapus(input).replace_triples()
    else:
        reversed_input = input[::-1]
        if reversed_input.startswith('m'):
            return Kharchang(reversed_input).mutate()[::-1][::-1]
        elif reversed_input.startswith('sb'):
            return Bob(reversed_input).dna
        elif reversed_input.startswith('s') and not reversed_input.startswith('sb'):
            return Okhtapus(reversed_input).replace_triples()[::-1][::-1]
        else:
            return 'invalid input'

print(validate_input(input()))
