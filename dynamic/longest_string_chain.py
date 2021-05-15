
# O (n*m^2 + n(log)n) time | O(nm)space
def longestStringChain(strings):
	stringChains = {}
	for string in strings:
		stringChains[string] = {"nextString":"","maxChainLength" :1}
	#print(stringChains)
	
	sortedStrings = sorted(strings, key = len)
	#print(sortedStrings)
	for string in sortedStrings:
		findLongestStringChain(string, stringChains)
	return buildLongestStringChain(strings, stringChains)

def findLongestStringChain(string, stringChains):
	for i in range(len(string)):
		smallerString = getSmallerString(string,i)
		if smallerString not in stringChains:
			continue
		tryUpdateLongestStringChain(string, smallerString,stringChains)
		

def getSmallerString(string,index):
	return string[0:index] + string[index+1:]

def tryUpdateLongestStringChain(currentString, smallerString,stringChains):
	smallerStringChainLen = stringChains[smallerString]["maxChainLength"]
	currentStringChainLen = stringChains[currentString]["maxChainLength"]
	
	if smallerStringChainLen + 1 > currentStringChainLen:
		stringChains[currentString]["maxChainLength"] = smallerStringChainLen + 1
		stringChains[currentString]["nextString"] = smallerString
		
def buildLongestStringChain(strings, stringChains):
	maxChainLen = 0
	chainStartingString = ""
	for string in strings:
		if stringChains[string]["maxChainLength"] > maxChainLen:
			maxChainLen = stringChains[string]["maxChainLength"]
			chainStartingString = string
			
	resultLen = []
	currentString = chainStartingString
	while currentString != '':
		resultLen.append(currentString)
		currentString = stringChains[currentString]["nextString"]
	
	return [] if len(resultLen) == 1 else resultLen
		       
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
        expected = ["abcdef", "abcde", "abde", "ade", "ae"]
        self.assertEqual(longestStringChain(strings), expected)


if __name__ == "__main__":
    unittest.main()