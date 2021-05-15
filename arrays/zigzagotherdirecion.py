

def findDiagonalOrder(matrix):
        
        if len(matrix) == 0:
            return []
        
        ans = []
        row = col = 0
        h = len(matrix) -1
        w = len(matrix[0]) -1
        directionDown = True
        

        while not isOutOfBounds(col, row, h, w):
            ans.append(matrix[row][col])
            if directionDown:
                if col == w or row == 0:
                    directionDown = False
                    if col == w:
                        row +=1
                    else:
                        col +=1
                else:
                    row -=1
                    col +=1
            else:
                if col == 0 or row == h:
                    directionDown = True
                    if row == h:
                        col +=1
                    else:
                        row +=1
                else:
                    row += 1
                    col -= 1

            # if directionDown:

            #     if col == w: # at far right
            #         row += 1
            #         directionDown = False
            #     elif row == 0: # at first row
            #         col += 1
            #         directionDown = False
            #     else:
            #         row -= 1
            #         col += 1

            # else:
            #     if row == h: # last row
            #         col += 1
            #         directionDown = True
            #     elif col == 0: # far left
            #         row += 1
            #         directionDown = True
            #     else:
            #         row += 1
            #         col -= 1

        return ans

def isOutOfBounds(col, row, h, w):
    return row < 0 or row > h or col < 0  or col > w
    
array = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(findDiagonalOrder(array))
#Output:  [1,2,4,7,5,3,6,8,9]