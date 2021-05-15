'''given a string of length of 12 or smaller contains only digits write all possible 
ip addresses that can be created by inserting 3 dots"


IP addres is a sequence of four positive integers separated by dot
where each separate integer is within a range 0-255

IP address is invalid if any of individual integers contain leading zeroes.
For example: 198.162.0.1 is valid but 198.162.00.1 and 198.162.00.01 are not

valid IP is between 4 to 12 digits 32 bits 8 bits each section
'''


def validIPAddresses(string):
    # Write your code here.
    ipAddrFound =[]

    for i in range(1, min(len(string),4)):
        currentIPAddresParts =['','','','']
        currentIPAddresParts[0] = string[:i]
        if not isValidPart(currentIPAddresParts[0]):
            continue
        for j in range(i+1, i+ min(len(string) - i, 4)):
            currentIPAddresParts[1] = string[i:j]
            if not isValidPart(currentIPAddresParts[1]):
                continue 
            for k in range(j+1, j+ min(len(string) - j,4)):
                currentIPAddresParts[2] = string[j:k]
                currentIPAddresParts[3] = string[k:]
                if isValidPart(currentIPAddresParts[2]) and isValidPart(currentIPAddresParts[3]):
                    ipAddrFound.append(".".join(currentIPAddresParts)) 
                
    return 	ipAddrFound
	

def isValidPart(string):
	stringAsInt = int(string)
	if stringAsInt > 255:
		return False
	return len(string) == len(str(stringAsInt))

print(validIPAddresses("1921680"))