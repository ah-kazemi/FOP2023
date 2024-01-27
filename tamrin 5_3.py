class Soldier:
    def __init__(self, id, health, coordinate):
        self.id = id
        self.health = health
        self.coordinate = coordinate


class Melee(Soldier):
    def __init__(self, id, health, coordinate):
        super().__init__(id, health, coordinate)


class Archer(Soldier):
    def __init__(self, id, health, coordinate):
        super().__init__(id, health, coordinate)


class Game:
    def __init__(self, n):
        self.board = [{} for _ in range(2)]
        self.turn = 0
        self.size = n

    def new(self, soldier_type, id, x, y):
        if id in self.board[self.turn]:
            print("duplicate tag")
            return
        soldier = None
        if soldier_type == 'melee':
            soldier = Melee(id, 100, (x, y))
        elif soldier_type == 'archer':
            soldier = Archer(id, 100, (x, y))
        self.board[self.turn][id] = soldier
        self.turn = 1 - self.turn

    def move(self, id, direction):
        soldier = self.board[self.turn][id]
        x, y = soldier.coordinate
        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        if x < 0 or x > self.size or y < 0 or y > self.size:
            print("out of bounds")
            return
        soldier.coordinate = (x, y)
        self.turn = 1 - self.turn

    def hamiltonian_distance(self, coord1, coord2):
        return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

    def attack(self, attacker_id, target_id):
        attacker = self.board[self.turn][attacker_id]
        target = self.board[1 - self.turn][target_id]
        if isinstance(attacker, Archer) and self.hamiltonian_distance(attacker.coordinate, target.coordinate) > 2:
            print("the target is too far")
            return
        elif isinstance(attacker, Melee) and self.hamiltonian_distance(attacker.coordinate, target.coordinate) > 1:
            print("the target is too far")
            return
        if isinstance(attacker, Archer):
            target.health -= 10
        elif isinstance(attacker, Melee):
            target.health -= 20
        if target.health <= 0:
            del self.board[1 - self.turn][target_id]
            print("target eliminated")
            self.turn = 1 - self.turn
            return
        self.turn = 1 - self.turn

    def info(self, id):
        if id not in self.board[self.turn]:
            return "soldier does not exist"
        soldier = self.board[self.turn][id]
        self.turn = 1 - self.turn
        return f"health:  {soldier.health}\nlocation:  {soldier.coordinate[0]}  {soldier.coordinate[1]}"

    def status(self):
        total_health_1 = sum(soldier.health for soldier in self.board[0].values() if soldier is not None)
        total_health_2 = sum(soldier.health for soldier in self.board[1].values() if soldier is not None)
        if total_health_1 > total_health_2:
            return "Player 1"
        elif total_health_1 < total_health_2:
            return "Player 2"
        else:
            return "draw"


def main():
    n = int(input())
    game = Game(n)
    while True:
        command = input().split()
        command_str = ' '.join(command)
        if command[0] == 'new':
            soldier_type = command[1]
            id = int(command[2])
            x = int(command[3])
            y = int(command[4])
            game.new(soldier_type, id, x, y)
        elif command[0] == 'move':
            id = int(command[1])
            direction = command[2]
            game.move(id, direction)
        elif command[0] == 'attack':
            attacker_id = int(command[1])
            target_id = int(command[2])
            game.attack(attacker_id, target_id)
        elif command[0] == 'info':
            id = int(command[1])
            print(game.info(id))
        elif command_str == 'who is in the lead?':
                print(game.status())
        elif command[0] == 'end':
            break


main()
