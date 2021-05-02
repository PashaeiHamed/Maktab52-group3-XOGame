from typing import Literal, Union, Optional
import os
import ast

class _Player:
    def __init__(self, name: str, sign: Literal['x', 'o']) -> None:
        self.name = name
        self.sign = sign


class _XOTable:
    xo_map = {k: None for k in range(1, 10)}  # {1:x, 2: None, 3: o, ...}

    def __str__(self):
        map = self.xo_map
        return """
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
""".format(*[map[i] if map[i] else i for i in map])

    def mark(self, cell_no, sign: str):
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, "Enter a valid cell no [1, 9]"
        assert not self.xo_map[cell_no], "Cell is filled"
        sign = str(sign).lower()
        assert sign in 'xo', 'Invalid sign' + sign
        self.xo_map[cell_no] = sign


class _XOGame(_XOTable):
    class UnFinishedGameError(Exception):
        "winner: zamani raise mishe k, bazi tamoom nashode bahe, vali winner() ..."
        pass

    class FinishedGameError(Exception):
        "mark: dar zamin k bazi tamoom shde ..."
        pass

    class InvalidCellError(Exception):
        "mark: Che por bashe, che addesh eshtabah bashe va ..."
        pass

    class InvalidPlayer(Exception):
        "mark: palyere voroodi eshtebah bashad!!!"
        pass

    def __init__(self, player1: _Player, player2: _Player) -> None:
        self.player1 = player1
        self.player2 = player2

    def _calculate_result(self):
        winner_id = self.winner().name
        loser_id = self.player1.name if self.player1.name != self.winner().name else self.player2.name
        print(loser_id)
        if os.path.exists("result.txt"):
            with open("result.txt", 'r') as file:
                data = str(file.read())
                result = ast.literal_eval(data)
                result.update({winner_id: result.get(winner_id, 0) + 1})
                result.update({loser_id: result.get(loser_id, 0)})
            with open("result.txt", 'w') as file:
                file.write(str(result))
        else:
            with open("result.txt", 'w') as file:
                result = {}
                result.update({winner_id: 1})
                result.update({loser_id: 0})
                file.write(str(result))
        return f'The score is : \n {list(result.keys())[0]} {result[self.player1.name]} - {result[self.player2.name]} {list(result.keys())[1]}'


def mark(self, cell_no, player: Union[_Player, Literal['x', 'o'], int]):
        super().mark(cell_no, player.sign)

    def winner(self) -> Optional[_Player]:
        if self.xo_map[7] == self.xo_map[8] == self.xo_map[9] != None:  # across the top
            return self.player1 if self.xo_map[7] == self.player1.sign else self.player2

        elif self.xo_map[4] == self.xo_map[5] == self.xo_map[6] != None:  # across the middle
            return self.player1 if self.xo_map[4] == self.player1.sign else self.player2

        elif self.xo_map[1] == self.xo_map[2] == self.xo_map[3] != None:  # across the bottom
            return self.player1 if self.xo_map[1] == self.player1.sign else self.player2

        elif self.xo_map[1] == self.xo_map[4] == self.xo_map[7] != None:  # down the left side
            return self.player1 if self.xo_map[1] == self.player1.sign else self.player2

        elif self.xo_map[2] == self.xo_map[5] == self.xo_map[8] != None:  # down the middle
            return self.player1 if self.xo_map[2] == self.player1.sign else self.player2

        elif self.xo_map[3] == self.xo_map[6] == self.xo_map[9] != None:  # down the right side
            return self.player1 if self.xo_map[3] == self.player1.sign else self.player2

        elif self.xo_map[7] == self.xo_map[5] == self.xo_map[3] != None:  # diagonal
            return self.player1 if self.xo_map[7] == self.player1.sign else self.player2

        elif self.xo_map[1] == self.xo_map[5] == self.xo_map[9] != None:  # diagonal
            return self.player1 if self.xo_map[1] == self.player1.sign else self.player2

players = [_Player('P1', 'x'), _Player('P2', 'o')]
game = _XOGame(*players)
table = _XOTable()
counter = 0
game_over = 0
print(table)

while True:
    for j in players:
        move = int(input(f'{j.name}'))
        game.mark(move, j)
        print(_XOTable())
        counter += 1
        if counter >= 5:
            if game.winner():
                print(f'{game.winner().name} is the winner')
                game_over = 1
                print(game._calculate_result())
                break

    if game_over:
        break
else:
    print("No winner")
