#wizard
#time O(nlogn)
import collections
import heapq

def find_shortest(wizards,start,dst):
	
	inb = {}
	
	for i in xrange(len(wizards)):
		inb[i] = wizards[i]
	heap = []
	if start not in inb:
		return -1
	for nxt in inb[start]:
		heapq.heappush(heap, (pow(nxt-start,2),(nxt)))

	while heap:
		curcost, (end) = heapq.heappop(heap)
		if end == dst:
			return curcost
		if inb[end]:
			for nxt in inb[end]:
				heapq.heappush(heap,(curcost+pow(nxt-end,2),(nxt)))
	return -1



if __name__ == "__main__":
	wizards = [[1,2],[3],[3,4],[4],[5]]

	print(find_shortest(wizards,0,4))
	
	






