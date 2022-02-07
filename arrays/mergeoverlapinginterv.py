def mergeOverlappingIntervals(a):
    sortedIntervals = sorted(a, key=lambda x:x[0])

    mergedIntervals =[]
    curInterval = sortedIntervals[0]    
    mergedIntervals.append(curInterval)

    for nextInterval in sortedIntervals:
        _, curIntEnd = curInterval
        nextStart, nextEnd = nextInterval
        if curIntEnd >= nextStart:
            curInterval[1] = max(curIntEnd, nextEnd)
        else:
            curInterval = nextInterval
            mergedIntervals.append(curInterval)
    return mergedIntervals

import unittest

class Test(unittest.TestCase):
    def test_case1(self):
        intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
        expected = [[1, 2], [3, 8], [9, 10]]
        actual = mergeOverlappingIntervals(intervals)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

        


