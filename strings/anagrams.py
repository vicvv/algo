'''return all anagrams from the strings provided'''

words = ['yo', 'act', 'flop', 'tac','cat', 'oy', 'olfp']
#answer = [['yo','oy'],['tac','cat', 'act'],['flop','olfp]]

# O(w * n * nlogn) time | O(w*n) space
def groupAnagrams(words):
    h = {}
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord in h:
            h[sortedWord].append(word)
        else:
            h[sortedWord] = [word]
        
    return list(h.values())

#print(groupAnagrams(words))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
        output = list(map(lambda x: sorted(x), groupAnagrams(words)))

        self.compare(expected, output)

    def compare(self, expected, output):
        if len(expected) == 0:
            self.assertEqual(output, expected)
            return
        self.assertEqual(len(expected), len(output))
        for group in expected:
            self.assertTrue(sorted(group) in output)

if __name__ == "__main__":
    unittest.main()