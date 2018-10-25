#regular_expression
def reg(source,pattern):
	if len(pattern) == 0 : return len(source) == 0
	if len(pattern) == 1: 
		if len(source) > 1 or len(source) == 0: 
			return False
		else:
			return source[0] == pattern[0]
	print(source, pattern)

	first_match = bool(source) and (source[0] == pattern[0] or pattern[0] == ".")
    
	if first_match or pattern[0] == "*":
		if pattern[1] == "*":
			#multiple or none
			return reg(source[1:], pattern) or reg(source, pattern[2:])

		elif pattern[1] == "+":
			return reg(source[1:], pattern) or reg(source[1:], pattern[2:])

		else:
			return reg(source[1:], pattern[1:])
	return pattern[1] == "*" and reg(source, pattern[2:])

if __name__ == "__main__":
	print(reg("a", "ac*"))
	print(reg("mississippi","mis*is*p*."))
	print(reg("mississipppi","mis*is*ip+i"))
	print(reg("misssddd","miss+ddd"))

