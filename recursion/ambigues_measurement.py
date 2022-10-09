'''This problem deals with measuring cups that are missing important measuring labels.
Specifically, a measuring cup only has two measuring lines, a Low (L) line and a High (H)
line. This means that these cups can't precisely measure and can only guarantee that
the substance poured into them will be between the L and H line. For example, you
might have a measuring cup that has a Low line at 400ml and a high line at 435ml .
This means that when you use this measuring cup, you can only be sure that what
you're measuring is between 400ml and 435ml .
You're given a list of measuring cups containing their low and high lines as well as one
low integer and one high integer representing a range for a target measurement.
Write a function that returns a boolean representing whether you can use the cups to
accurately measure a volume in the specified [low, high] range (the range is
inclusive).
Note that:Each measuring cup will be represented by a pair of positive integers [L, H],
where 0 <= L <= H .
You'll always be given at least one measuring cup, and the low and high
input parameters will always satisfy the following constraint:
0 <= low <= high .
Once you've measured some liquid, it will immediately be transferred to a larger
bowl that will eventually (possibly) contain the target measurement.
You can't pour the contents of one measuring cup into another cup'''

# O(low * high * n) time | O(low * high) space - where n is the numb
def ambiguousMeasurements(measuringCups, low, high):
    memoization = {}
    return canMeasureInRange(measuringCups, low, high, memoization)
def canMeasureInRange(measuringCups, low, high, memoization):
    memoizeKey = createHashableKey(low, high)
    if memoizeKey in memoization:
        return memoization[memoizeKey]
    if low <= 0 and high <= 0:
        return False
    canMeasure = False
    for cup in measuringCups:
        cupLow, cupHigh = cup
        if low <= cupLow and cupHigh <= high:
            canMeasure = True
            break
        newLow = max(0, low - cupLow)
        newHigh = max(0, high - cupHigh)
        canMeasure = canMeasureInRange(measuringCups, newLow, newHigh, memoization)
        if canMeasure:
            break
    memoization[memoizeKey] = canMeasure
    return canMeasure

def createHashableKey(low, high):
    return str(low) + ":" + str(high)


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        cups = [[200, 210], [450, 465], [800, 850]]
        low = 2100
        high = 2300
        expected = True
        actual = ambiguousMeasurements(cups, low, high)
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()