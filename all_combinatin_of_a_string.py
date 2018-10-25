#combination_
#-*- coding: utf-8 -*-
def all_combination_of_string(source):
	
	queue = [source]
	visited = set()
	visited.add(source)
	res = []
	i = 0
	while i < len(source):
		size = len(queue)
		for j in xrange(size):
			cur = queue.pop(0)
			res.append(cur)

			lower = cur[i].lower()
			upper = cur[i].upper()
			newu = cur[:i] + upper + cur[i+1:]
			newl = cur[:i] + lower + cur[i+1:]
			
			queue.append(newu)
			queue.append(newl)
		i +=1
	

	return queue

if __name__ == "__main__":
	source = "abc"
	print(all_combination_of_string(source))