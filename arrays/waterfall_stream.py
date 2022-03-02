'''
You're given a two-dimensional array that represents the
structure of an indoor waterfall and a positive integer that
represents the column that the waterfall's water source will start
at. More specifically, the water source will start directly above the
structure and will flow downwards.
Each row in the array contains 0 s and 1 s, where a 0
represents a free space and a 1 represents a block that water
can't pass through. You can imagine that the last row of the array
contains buckets that the water will eventually flow into; thus, the
last row of the array will always contain only 0 s. You can also
imagine that there are walls on both sides of the structure,
meaning that water will never leave the structure; it will either be
trapped against a wall or flow into one of the buckets in the last
row.
As water flows downwards, if it hits a block, it splits evenly to the
left and right-hand side of that block. In other words, 50% of the
water flows left and 50% of it flows right. If a water stream is
unable to flow to the left or to the right (because of a block or a
wall), the water stream in question becomes trapped and can no
longer continue to flow in that direction; it effectively gets stuck
in the structure and can no longer flow downwards, meaning that
50% of the previous water stream is forever lost.
Lastly, the input array will always contain at least two rows and
one column, and the space directly below the water source (in
the first row of the array) will always be empty, allowing the
water to start flowing downwards.
Write a function that returns the percentage of water inside each
of the bottom buckets after the water has flowed through the
entire structure.
You can refer to the first 4.5 minutes of this question's video
explanation for a visual example.




O(w^2 * h) time | O(w) space - where w and h are the width
and height of the input array
'''


def waterfallStreams(array, source):
    row_above = array[0][:]
    row_above[source] = -1

    for row in range(1, len(array)):
        current_row= array[row][:]
        
        for idx in range(len(row_above)):
            value_above = row_above[idx]
            has_water_above = value_above < 0
            has_block = current_row[idx] == 1
            
            if not has_water_above:
                continue
            
            if not has_block:
                current_row[idx] += value_above
                continue
            split_water = value_above / 2

            right_index = idx
            while right_index + 1 < len(row_above):
                right_index += 1
                if row_above[right_index] == 1: 
                    break
                if current_row[right_index] != 1: 
                    current_row[right_index] += split_water
                    break
            
            left_index = idx
            while left_index - 1 >= 0:
                left_index -= 1
                if row_above[left_index] == 1: 
                    break
                if current_row[left_index] != 1:
                    current_row[left_index] += split_water
                    break
        row_above = current_row

    finalPercentages = list(map(lambda num: num * -100, row_above))
    return finalPercentages


# def waterfallStreams(array, source):
#     row_above = array[0][:]
#     # We'll use -1 to represent water, since 1 is used for a block.
#     row_above[source] = -1
#     for row in range(1, len(array)):
#         current_row= array[row][:]

#     for idx in range(len(row_above)):
#         value_above = row_above[idx]
#         has_water_above = value_above < 0
#         has_block = current_row[idx] == 1
#         if not has_water_above:
#             continue
#         if not has_block:
#         # If there is no block in the current column, move the water down.
#             current_row[idx] += value_above
#             continue
#         split_water = value_above / 2
#         # Move water right.
#         right_index = idx
#         while right_index + 1 < len(row_above):
#             right_index += 1
#             if row_above[right_index] == 1: # if there is a block in the way
#                 break
#             if current_row[right_index] != 1: # if there is no block below us
#                 current_row[right_index] += split_water
#                 break
#         # Move water left.
#         left_index = idx
#         while left_index - 1 >= 0:
#             left_index -= 1
#             if row_above[left_index] == 1: # if there is a block in the way
#                 break
#             if current_row[left_index] != 1: # if there is no block below us
#                 current_row[left_index] += split_water
#                 break
#     row_above = current_row
#     # Convert our negative values to positive percentages.
#     finalPercentages = list(map(lambda num: num * -100, row_above))
#     return finalPercentages


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
        ]
        source = 3
        expected = [0, 0, 0, 25, 25, 0, 0]
        actual = waterfallStreams(array, source)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()