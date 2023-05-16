import random


class xox:
    def __init__(self):
        self.data = ['-']*9

    def get(self, a):
        return self.data[a]

    def change(self, a, l):
        if self.data[a] == '-':
            self.data[a] = l

    def restart(self):
        self.data = ['-']*9

    def isWinner(self, bo, le):
        return ((bo[6] == le and bo[7] == le and bo[8] == le) or (bo[3] == le and bo[4] == le and bo[5] == le) or (bo[0] == le and bo[1] == le and bo[2] == le) or (bo[6] == le and bo[3] == le and bo[0] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[6] == le and bo[4] == le and bo[2] == le) or (bo[8] == le and bo[4] == le and bo[0] == le))

    def getBoardCopy(self):
        dupeBoard = []
        for i in self.data:
            dupeBoard.append(i)
        return dupeBoard

    def isSpaceFree(self, board, move):
        return board[move] == '-'

    def makeMove(self, board, letter, move):
        board[move] = letter

    def chooseRandomMoveFromList(self, movesList):
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(self.data, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(self):
        computerLetter = 'O'
        playerLetter = 'X'
        for i in range(0, 9):
            copy = self.getBoardCopy()
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, computerLetter, i)
                if self.isWinner(copy, computerLetter):
                    return i
        for i in range(0, 9):
            copy = self.getBoardCopy()
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, playerLetter, i)
                if self.isWinner(copy, playerLetter):
                    return i
        move = self.chooseRandomMoveFromList([0, 2, 6, 8])
        if move != None:
            return move
        if self.isSpaceFree(self.data, 4):
            return 4
        return self.chooseRandomMoveFromList([1, 3, 5, 7])

    def isBoardFull(self):
        for i in range(0, 9):
            if self.isSpaceFree(self.data, i):
                return False
        return True
