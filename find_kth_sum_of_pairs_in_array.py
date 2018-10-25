#find kth sum of pairs in array
#time O(nlogn)
#space O(n)
import heapq
def find_kth(arr,k):

	arr = sorted(arr)
	heap = []
	for i in xrange(1,len(arr)):
		heap.append((arr[0]+arr[i],(0,i)))
	heapq.heapify(heap)
	for i in xrange(k):
		if heap:
			cursum, (i,j) = heapq.heappop(heap)
			if i+1 < len(arr):
				heapq.heappush(heap,(arr[i+1]+arr[j],(i+1,j)))
		else:
			cursum = None

	return cursum

print(find_kth([2,4,6,8,10,11],4))






