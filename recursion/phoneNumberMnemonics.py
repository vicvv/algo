import unittest

h ={
		"0":["0"],
		"1":["1"],
		"2":["a", "b","c"],
		"3":["d","e","f"],
		"4":['g','h','i'],
		"5":['j','k','l'],
		"6":['m','n','o'],
		"7":['p','q','r','s'],
		"8":['t','u','v'],
		"9":['w','x','y','z']
	}
def phoneNumberMnemonics(ph):
      
    mnemonicsFound =[]
    currentMnemonics =["0"]*4

    phHelper(0, ph, currentMnemonics, mnemonicsFound)

    return mnemonicsFound

def phHelper(idx, ph, currentMnemonics, mnemonicsFound):
    if idx == len(ph):
        mnemonics = ''.join(currentMnemonics)
        mnemonicsFound.append(mnemonics)

    else:
        for letter in h[ph[idx]]:
            currentMnemonics[idx]=letter
            phHelper(idx+1, ph, currentMnemonics, mnemonicsFound)


        

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        phoneNumber = "1905"
        expected = ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
        actual = phoneNumberMnemonics(phoneNumber)
        self.assertEqual(actual, expected)

if __name__ =='__main__':
    unittest.main()

