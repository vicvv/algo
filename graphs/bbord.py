# time O (ws + nm)
# space O(ws) (for building the trie) + nm ( for building visited)


'''
You're given a two-dimensional array (a matrix) of potentially unequal height and width 
containing letters; this matrix represents a boggle board. You're also given a list of words.
Write a function that returns an array of all the words contained in the boggle board. 
The final words don't need to be in any particular order.A word is constructed in the boggle 
board by connecting adjacent (horizontally, vertically, 
or diagonally) letters, without using any single letter at
a given position more than once; while a word can of course have repeated letters, 
those repeated letters must come from different positions
in the boggle board in order for the word to be contained in the board. Note that 
two or more words are allowed to overlap and use the same
letters in the boggle board.
Sample Input
board = [
 ["t", "h", "i", "s", "i", "s", "a"],
 ["s", "i", "m", "p", "l", "e", "x"],
 ["b", "x", "x", "x", "x", "e", "b"],
 ["x", "o", "g", "g", "l", "x", "o"],
 ["x", "x", "x", "D", "T", "r", "a"],
 ["R", "E", "P", "E", "A", "d", "x"],
 ["x", "x", "x", "x", "x", "x", "x"],
 ["N", "O", "T", "R", "E", "-", "P"],
 ["x", "x", "D", "E", "T", "A", "E"],
],
words = [
 "this", "is", "not", "a", "simple", "boggle",
 "board", "test", "REPEATED", "NOTRE-PEATED",
'''
'''
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for lettern in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trie, visited, finalWords):
    if visited[i][j] == True:
        return
    letter = board[i][j]
    if letter not in trie:
        return
    visited[i][j] = True
    trieNode = trie[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbours = getNeighbours(i, j, board)
    for neighbour in neighbours:
        explore(neighbour[0], neighbour[1], board, trieNode, visited, finalWords)
    visited[i][j] = False


def getNeighbours(i, j, board):
    neighbours = []
    possibleDirections = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for direction in possibleDirections:
        di, dj = direction
        newI, newJ = i + di, j + dj
        if 0 <= newI < len(board) and 0 <= newJ < len(board[0]):
            neighbours.append([newI, newJ])
    return neighbours


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
'''

def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for value in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())

def explore(i, j, board, trieNode, visited ,finalWords,):
    if visited[i][j]:
        return
    letter = board[i][j]
    
    if letter not in trieNode:
        return
    visited[i][j] = True

    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
        print(finalWords)
    neigbours = getNeigbours(i,j, board)
    for neigbour in neigbours:
        explore(neigbour[0], neigbour[1], board, trieNode, visited, finalWords)
    visited[i][j] = False
	
	
def getNeigbours(i,j, board):
    neigbours = []
    if i > 0 and j > 0:
        neigbours.append([i-1,j-1])
    if i > 0 and j < len(board[0]) -1:
        neigbours.append([i - 1, j + 1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neigbours.append([i+1,j+1])
    if i < len(board) - 1 and j > 0:
        neigbours.append([i+1, j-1])
    if i > 0:
        neigbours.append([i-1,j])
    if i < len(board) - 1:
        neigbours.append([i+1,j])
    if j > 0:
        neigbours.append([i,j-1])
    if j < len(board[0]) - 1:
        neigbours.append([i,j+1])
    return neigbours
	
		

class Trie:
	def __init__(self):
		self.root = {}
		self.endSumbol = "*"
	
	def add(self, word):
		current = self.root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[self.endSumbol] = word
		
		
		
		
		
		
		
		
		
		


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        board = [
            ["t", "h", "i", "s", "i", "s", "a"],
            ["s", "i", "m", "p", "l", "e", "x"],
            ["b", "x", "x", "x", "x", "e", "b"],
            ["x", "o", "g", "g", "l", "x", "o"],
            ["x", "x", "x", "D", "T", "r", "a"],
            ["R", "E", "P", "E", "A", "d", "x"],
            ["x", "x", "x", "x", "x", "x", "x"],
            ["N", "O", "T", "R", "E", "-", "P"],
            ["x", "x", "D", "E", "T", "A", "E"],
        ]
        words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]
        expected = ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
        actual = boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

if __name__ == "__main__":
    unittest.main()