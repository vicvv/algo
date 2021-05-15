#[width,depth, hegith] 
# The goal is to stack up the disk and maximaze the total hegith of
# the stack. The disk must have strictly samller weight, height and width that one below it.

def diskStacking(disks):
    disks.sort(key=lambda disk:disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    maxHeightsIdx = 0
        
    for i in range(1, len(disks)):
        curDisk = disks[i]

        for j in range(0,i):
            otherDisk = disks[j]
            if areValidDims(otherDisk,curDisk):
                print(curDisk[2], heights[j])
                if heights[i] <= curDisk[2] + heights[j]:
                    heights[i] = curDisk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[maxHeightsIdx] :
            maxHeightsIdx = i
            
    return buildSeq(disks, sequences, maxHeightsIdx)

def buildSeq(disks, sequences, curIdx):
	seq = []
	while curIdx is not None:
		seq.append(disks[curIdx])
		curIdx = sequences[curIdx]
	return list(reversed(seq))
							
						
def areValidDims(o,c):
	return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

import unittest

class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]),[[2,1,2],[3,2,3],[4,4,5]])
    def test2(self):
        self.assertEqual(diskStacking([[2, 1, 2], [3, 2, 3], [2, 3, 4]]),[[2,1,2],[3,2,3]])
if __name__ == "__main__":
    unittest.main()