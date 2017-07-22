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
            'a':1}
            
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

class Game (object):
    def __init__(self, file):
        self.cols = [[] for i in range(nCols)]
        self.freeCols = [False]*nCols
        self.cells = [None]*nCells
        self.foundations = [None]*nFoundations
        for i in range(nInitRows):
            line = gameFile.readline().split()
            for j in range(len(line)):
                self.cols[j].append(Card(line[j]))
                
    def __str__(self):
        out = '\n'
        maxD = self.maxDepth()
        out += (' '.join((str(i) if i != None else 'x '\
                for i in self.cells)) + ' ')
        out += ' '.join((str(i)if i != None else '0 '\
                for i in self.foundations))
        out += '\n\n'
        out += ''.join(' '.join((self.cols[j][i].__str__()\
                if i < len((self.cols[j])) else '  '\
                for j in range(nCols))) + '\n' for i in range(maxD))
        return out
        
    def maxDepth(self):
        return max((len(i) for i in self.cols))

gameFile = open('game.txt')
newGame = Game(gameFile)
gameFile.close()
print(newGame, end = '')
