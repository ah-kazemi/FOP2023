# import matplotlib.pyplot as plt
# import pandas as pd


def get_input(expected_length):
    value = input().split()
    if len(value) != expected_length:
        print("Invalid Command.")
        exit(0)
    return value

try:
    name1, name2 = get_input(2)
    health1, health2 = map(int, get_input(2))
    damageA, damageB, damageC = map(int, get_input(3))
    card1_1, card1_2 = get_input(2)
    card2_1, card2_2 = get_input(2)
    card3_1, card3_2 = get_input(2)
except ValueError:
    print("Invalid Command.")
    exit(0)


def get_damage(card):
    if card == 'A':
        return damageA
    elif card == 'B':
        return damageB
    elif card == 'C':
        return damageC


score1 = 0
score2 = 0

if (name1 is not None) & (name2 is not None) & (card1_1 is not None) & (card1_2 is not None) & (card2_1 is not None) & (card2_2 is not None) & (card3_1 is not None) & (card3_2 is not None) & (health1 is not None) & (health2 is not None):
    damage1_1 = get_damage(card1_1)
    damage1_2 = get_damage(card1_2)
    damage2_1 = get_damage(card2_1)
    damage2_2 = get_damage(card2_2)
    damage3_1 = get_damage(card3_1)
    damage3_2 = get_damage(card3_2)
    health1 -= (damage1_2 + damage2_2 + damage3_2)
    health2 -= (damage1_1 + damage2_1 + damage3_1)
    score1 += (damage1_1 > damage1_2)
    score1 += (damage2_1 > damage2_2)
    score1 += (damage3_1 > damage3_2)
    score2 += (damage1_2 > damage1_1)
    score2 += (damage2_2 > damage2_1)
    score2 += (damage3_2 > damage3_1)

    print(f"{name1} -> Score: {score1}, Health: {health1}")
    print(f"{name2} -> Score: {score2}, Health: {health2}")

"""
    with open('result.txt', 'w') as f:
        f.write(f"{name1} -> Score: {score1}, Health: {health1}\n")
        f.write(f"{name2} -> Score: {score2}, Health: {health2}\n")

    df = pd.DataFrame({'players': ['Player 1', 'Player 2'], 'scores': [score1, score2]})

    df.plot(kind='bar', x='players', y='scores', legend=False)
    plt.ylabel('Scores')
    plt.title('Scores by player')
    plt.tight_layout()
    plt.show()
"""