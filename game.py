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
    def __init__(self, file):
        self.cols = [[] for i in range(nCols)]
        self.freeCols = [False]*nCols
        self.cells = [None]*nCells
        self.foundations = [0]*nFoundations
        for i in range(nInitRows):
            line = gameFile.readline().split()
            for j in range(len(line)):
                self.cols[j].append(Card(line[j]))
                
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
        
    def colToCell(self, col):
        try:
            i = self.cells.index(None)
            self.cells[i] = self.cols[col].pop()
            return True
        except ValueError:
            return False
        
    def colToFoundation(self, col):
        try:
            tempCard = self.cols[col][-1]
            if self.foundations[tempCard.suit] == tempCard.value - 1:
                self.foundations[tempCard.suit] = self.cols[col].pop().value
                return True
            else:
                return False
        except IndexError:
            return False
            
    def colToCol(self, col, colBase):
        try:
            tempCard = self.cols[col][-1]
            if len(self.cols[colBase]):
                baseCard = self.cols[colBase][-1]
                if Game.cardCompatibility(tempCard, baseCard):
                    self.cols[colBase].append(self.cols[col].pop())
                    return True
                else:
                    return False
            else:   
                self.cols[colBase].append(self.cols[col].pop())
                return True
        except IndexError:
            return False

    def cellToCol(self, cell, col):
        cellCard = self.cells[cell]
        if cellCard:
            if len(self.cols[col]):
                baseCard = self.cols[col][-1]
                if Game.cardCompatibility(cellCard, baseCard):
                    self.cols[col].append(cellCard)
                    self.cells[cell] = None
                    return True
                else:
                    return False
            else:   
                self.cols[col].append(cellCard)
                self.cells[cell] = None
                return True
        else:
            return False
            
    def cellToFoundation(self, cell):
        cellCard = self.cells[cell]
        if cellCard:
            if self.foundations[cellCard.suit] == cellCard.value - 1:
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
    
    def maxDepth(self):
        return max((len(i) for i in self.cols))
        
    def isSolved(self):
        return all((len(i) == 0 for i in self.cols))

gameFile = open('game.txt')
newGame = Game(gameFile)
gameFile.close()

print(newGame, end = '')
