# This is an input class. Do not edit.
# time: O(d) d is the depth of lovest descendant
# space O(1)

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None
    
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(topAncestor, descendantOne)
    depthTwo = getDepth(topAncestor, descendantTwo)

    if depthOne > depthTwo:
        return getYoungest(descendantOne, descendantTwo, topAncestor, depthOne - depthTwo)
    else:
        return getYoungest(descendantTwo, descendantOne,  topAncestor, depthTwo - depthOne)

	
def getDepth(topAncestor, descendant):
    depth = 0
    while descendant != topAncestor:
        depth +=1
        descendant = descendant.ancestor
    return depth

def getYoungest(dlowest, dhighest, topAncestor, diffs):
	while diffs > 0:
		dlowest = dlowest.ancestor
		diffs -=1
	
	while dlowest != dhighest:
		dlowest = dlowest.ancestor
		dhighest = dhighest.ancestor
	return dlowest
	



# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!


import unittest


# class AncestralTree(AncestralTree):
#     def addDescendants(self, *descendants):
#         for descendant in descendants:
#             descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])

if __name__ == "__main__":
    unittest.main()