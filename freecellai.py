suitIDict = {'s':0,\
            'd':1,\
            'c':2,\
            'h':3}

valueIDict = {'k':13,\
            'q':12,\
            'j':11,\
            't':10,\
            '9':9,\
            '8':8,\
            '7':7,\
            '6':6,\
            '5':5,\
            '4':4,\
            '3':3,\
            '2':2,\
            'a':1,\
            '0':0}
            
suitSDict = {suitIDict[i]:i for i in suitIDict}
valueSDict = {valueIDict[i]:i for i in valueIDict}

inStringSuitKey = 0
inStringValueKey = 1

nCols = 8
nInitRows = 7
nCells = 4
nFoundations = 4

class Card (object):
    def __init__(self, s):
        self.suit = suitIDict[s[inStringSuitKey]]
        self.value = valueIDict[s[inStringValueKey]]
        
    def __str__(self):
        return suitSDict[self.suit] + valueSDict[self.value]
        
    def __repr__(self):
        return self.__str__()

class Game (object):
    def __init__(self, file = None, copy = None):
        if file:
            self.cols = [[] for i in range(nCols)]
            self.freeCols = [False]*nCols
            self.cells = [None]*nCells
            self.foundations = [0]*nFoundations
            for i in range(nInitRows):
                line = file.readline().split()
                for j in range(len(line)):
                    self.cols[j].append(Card(line[j]))
        elif copy:
            self.cols = [list(i) for i in copy.cols]
            self.freeCols = list(copy.freeCols)
            self.cells = list(copy.cells)
            self.foundations = list(copy.foundations)
    
    def command (self, sCommand):
        if len(sCommand) < 7 and len(sCommand) > 0:
            fro = sCommand[0:2]
            to = sCommand[2:4]
            if fro[0] == 'c':
                if to[0] == 'c':
                    if fro[1].isdigit() and to[1].isdigit():
                        return self.colToCol(int(fro[1]), int(to[1]))
                    else:
                        return False
                elif to[0] == 'a':
                    if fro[1].isdigit() and to[1].isdigit():
                        return self.colToCell(int(fro[1]), int(to[1]))
                    else:
                        return False
                elif to[0] == 'f':
                    if fro[1].isdigit():
                        return self.colToFoundation(int(fro[1]))
                    else:
                        return False
                else:
                    return False
            elif fro[0] == 'a':
                if to[0] == 'c':
                    if fro[1].isdigit() and to[1].isdigit():
                        return self.cellToCol(int(fro[1]), int(to[1]))
                    else:
                        return False
                elif to[0] == 'f':
                    if fro[1].isdigit():
                        return self.cellToFoundation(int(fro[1]))
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def colToCell(self, col, cell, goAhead = True):
        try:
            tempCard = self.cols[col][-1]
            if self.cells[cell]:
                return False
            else:
                if goAhead:
                    self.cells[cell] = self.cols[col].pop()
                return True
        except IndexError:
            return False
        
    def colToFoundation(self, col, goAhead = True):
        try:
            tempCard = self.cols[col][-1]
            if self.foundations[tempCard.suit] == tempCard.value - 1:
                if goAhead:
                    self.foundations[tempCard.suit] = self.cols[col].pop().value
                return True
            else:
                return False
        except IndexError:
            return False
            
    def colToCol(self, col, colBase, goAhead = True):
        try:
            tempCard = self.cols[col][-1]
            if len(self.cols[colBase]):
                baseCard = self.cols[colBase][-1]
                if Game.cardCompatibility(tempCard, baseCard):
                    if goAhead:
                        self.cols[colBase].append(self.cols[col].pop())
                    return True
                else:
                    return False
            else: 
                if goAhead:
                    self.cols[colBase].append(self.cols[col].pop())
                return True
        except IndexError:
            return False

    def cellToCol(self, cell, col, goAhead = True):
        cellCard = self.cells[cell]
        if cellCard:
            if len(self.cols[col]):
                baseCard = self.cols[col][-1]
                if Game.cardCompatibility(cellCard, baseCard):
                    if goAhead:
                        self.cols[col].append(cellCard)
                        self.cells[cell] = None
                    return True
                else:
                    return False
            else:  
                if goAhead:
                    self.cols[col].append(cellCard)
                    self.cells[cell] = None
                return True
        else:
            return False
            
    def cellToFoundation(self, cell, goAhead = True):
        cellCard = self.cells[cell]
        if cellCard:
            if self.foundations[cellCard.suit] == cellCard.value - 1:
                if goAhead:
                    self.foundations[cellCard.suit] = cellCard.value
                    self.cells[cell] = None
                return True
            else:
                return False
        else:
            return False            
        
    def cardCompatibility(newCard, baseCard):
        if newCard.suit % 2 != baseCard.suit % 2:
            if baseCard.value == newCard.value + 1:
                return True
            else:
                return False
        else:
            return False
            
    def emptyCell(self):
        try:
            return self.cells.index(None)
        except ValueError:
            return None
    
    def maxDepth(self):
        return max((len(i) for i in self.cols))
        
    def isSolved(self):
        return all((len(i) == 0 for i in self.cols))

    def __str__(self):
        out = '\n'
        maxD = self.maxDepth()
        out += (' '.join((str(i) if i else 'x '\
                for i in self.cells)) + '|')
        out += ' '.join((suitSDict[i] + valueSDict[self.foundations[i]] \
                for i in range(nFoundations)))
        out += '\n\n'
        out += ''.join(' '.join((str(self.cols[j][i]) \
                if i < len((self.cols[j])) else '  '\
                for j in range(nCols))) + '\n' for i in range(maxD))
        return out
    
def allPossibleMoves(game):
    ret = []
    ret += ['c' + str(i) + 'f' \
        for i in range(nCols) if game.colToFoundation(i, False)]
    ret += ['a' + str(i) + 'f' \
        for i in range(nCells) if game.cellToFoundation(i, False)]
    nextEmptyCell = game.emptyCell()
    ret += ['c' + str(i) + 'c' + str(j)\
        for i in range(nCols) for j in range(nCols)\
        if i != j if game.colToCol(i, j, False)]
    ret += ['a' + str(i) + 'c' + str(j)\
        for i in range(nCells) for j in range(nCols)\
        if game.cellToCol(i, j, False)]
    if nextEmptyCell != None:
        ret += ['c' + str(i) + 'a' + str(nextEmptyCell)
            for i in range(nCols) if game.colToCell(i, nextEmptyCell, False)]
    return ret
    
def ai(game):
    gameStack = [Game(copy = game)]
    commandStack = [allPossibleMoves(game)]
    moveStack = [commandStack[0][0]]
    repStack = []
    
    
if __name__ == "__main__":
    gameFile = open('game.txt')
    newGame = Game(file = gameFile)
    cmd = ''
    while not newGame.isSolved() and cmd != 'exit':
        print(newGame, end = '')
        print ('>>', end = '')
        cmd = input()
        if cmd != 'exit' and cmd != 'ai':
            if not newGame.command(cmd):
                print('\nInvalid Input')
        elif cmd == 'ai':
            print(ai(newGame))
    if cmd != 'exit':
        print('You Win')
