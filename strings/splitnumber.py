def expanded_form(num):
	ret = []
	k = 1
	while num > 0:
		num, r = divmod(num, 10)
		if r > 0:
			ret.append(r*k)
		k *= 10
	return " + ".join(map(str, ret[::-1]))

print(expanded_form(12))