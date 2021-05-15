'''
repetition("ab", 3) ➞ "ababab"
repetition("kiwi", 1) ➞ "kiwi"
repetition("cherry", 2) ➞ "cherrycherry"
'''


def repetition(txt, n):
	return '' if not n else txt + repetition(txt, n-1)