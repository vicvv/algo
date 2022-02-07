#return the array of indices of the building that can see the sunset
# the building can see sunset if it is strictly taller than all the buildings that come ofter it

def sunsetViews(buildings, direction):
    curmax,rmax,res = 0,0,[]
    
    start = 0 if direction == 'WEST' else len(buildings)-1
    limit = len(buildings) if start == 0 else -1
    step = 1 if start==0 else -1
    print(start, limit, step)
    for i in range(start, limit, step):
        rmax = max(rmax, buildings[i])
        if rmax > curmax:
            curmax = rmax
            res.append(i)

    return sorted(res)


print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2],"WEST"))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "EAST"
        expected = [1, 3, 6, 7]
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "WEST"
        expected = [0,1]
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()