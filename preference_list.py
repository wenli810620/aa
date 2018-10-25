#preference_list
import collections
def preference_list(source):

	oub = collections.defaultdict(set)
	inb = collections.defaultdict(int)
	ch_set = set()
	queue = []
	for s in source:
		for i in xrange(len(s)-1):
			oub[s[i]].add(s[i+1])
			inb[s[i+1]] +=1
			ch_set.add(s[i])
			ch_set.add(s[i+1])
   
	for ch in ch_set:
		if inb[ch] == 0:
			queue.append(ch)
	ans = []
	while queue:
		cur = queue.pop(0)
		ans.append(cur)
		if oub[cur]:
			for v in oub[cur]:
				inb[v] -=1
				if inb[v] == 0:
					queue.append(v)
	return ans
	
if __name__ == "__main__":
	print(preference_list([[3, 5, 7, 9], [2, 3, 8], [5, 8]]))