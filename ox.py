from typing import Literal, Union, Optional


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
        pass

    def mark(self, cell_no, player: Union[_Player, Literal['x', 'o'], int]):
        pass

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
