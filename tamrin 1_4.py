def check_invitation(invitation_list, person):
    if invitation_list & (1 << person) != 0:
        return "yes"
    else:
        return "no"


invitation_list_right = int(input()) & 0xFFFFFFFF
invitation_list_left = int(input()) & 0xFFFFFFFF
n = int(input())

results = []

persons = []
for _ in range(n):
    person = int(input())
    persons.append(person)

invitation_list = (invitation_list_left << 32) | invitation_list_right

for person in persons:
    result = check_invitation(invitation_list, person)
    results.append(result)

print("\n".join(results))
