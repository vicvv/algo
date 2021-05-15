'''
given coints return min ammount of change that you can not return
for example coins = [1,2,5]. min ammount that you cant return is 4

'''
coints = [5, 7, 1, 1, 2, 3, 22]
#coints = [1,2,5] # cant make 4 coints

def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for coin in coints:
        print(coin,currentChange + 1 )
        if coin > currentChange + 1:
            return currentChange + 1
        currentChange += coin
    return currentChange + 1

print(nonConstructibleChange(coints))

import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        acctual = nonConstructibleChange(input)
        self.assertEqual(expected, acctual)


# if __name__ == "__main__":
#     unittest.main()

    
    