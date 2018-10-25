#-*- coding: utf-8 -*-
'''题目是给一个转换规则来转换数字n
n是奇数 n = 3n + 1
n是偶数 n = n / 2

最后n总会经过很多次转换到1

问从一到一百万 需要转换次数最多的那个数字需要转换几次'''

def find_step(num,map_dict):
	if num <= 1:
		return 1
	if num in map_dict: return map_dict[num]
	if num % 2 == 0: 
		return find_step(num/2,map_dict) + 1
	else:
		return find_step(num*3 + 1,map_dict) + 1

def find_longest_step(num):
	map_dict = {}
	max_res = 0
	for i in xrange(1,num+1):
		res = find_step_iterative(i, map_dict)
		map_dict[i] = res
		max_res = max(max_res, res)
	return max_res

def find_step_iterative(n,map_dict):
	
	count = 0
	while n != 1:
		if n in map_dict : 
			return map_dict[n] + count
		if n % 2 == 0:
			n /=2
		else:
			n = n*3 + 1
		count +=1
	return count 
		
if __name__ == "__main__":
	num = 1000000
	print(find_longest_step(num))


