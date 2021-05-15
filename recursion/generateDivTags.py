# function takes a positive integer and returns all the posible valid strings that you 
# can generate with <div> tag

# O((2N)!)/((n!((n+1)))) Time | O((2N)!)/((n!((n+1)))) space where N is a number of inputs

def generateDivTags(numberOfTags):
    matchingtags = []
    generateTags(numberOfTags, numberOfTags,"", matchingtags)
    return matchingtags


def generateTags(openingTagsNeeded, closingTagsNeeded,prefix, result):
    if openingTagsNeeded > 0:
        newprefix = prefix + "<div>"
        generateTags(openingTagsNeeded-1, closingTagsNeeded,newprefix, result)
    if openingTagsNeeded < closingTagsNeeded:
        newprefix = prefix + "</div>"
        generateTags(openingTagsNeeded, closingTagsNeeded-1,newprefix, result)
        
    if closingTagsNeeded == 0:
        result.append(prefix)



import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = 3
        expected = [
            "<div><div><div></div></div></div>",
            "<div><div></div><div></div></div>",
            "<div><div></div></div><div></div>",
            "<div></div><div><div></div></div>",
            "<div></div><div></div><div></div>",
        ]
        actual = generateDivTags(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()