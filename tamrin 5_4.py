import string

n = int(input())
sentence = input().translate(str.maketrans('', '', string.punctuation + '،')).split()
word = input()

for s in sentence:
    original_s = s
    if len(s) < len(word):
        s += '_' * (len(word) - len(s))
    elif len(word) < len(s):
        word += '_' * (len(s) - len(word))

    differences = sum([s[i] != word[i] for i in range(len(s))])
    if differences <= n:
        print(original_s)