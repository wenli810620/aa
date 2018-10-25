#meeting_room 
import heapq
def meeting(meetings,k):
	heap = []
	for m in meetings:
		for interval in m:
			heapq.heappush(heap,(interval[0],True))
			heapq.heappush(heap,(interval[1],False))
	cnt = 0
	res = []
	start_time = None
	i = 0
	t_len = len(meetings)
	points_len = len(heap)
	
	while heap:
		cur,cur_status = heapq.heappop(heap)


		if cur_status == True:
			
			cnt += 1
			if start_time is None and i == 0 and cnt <= t_len - k:
				start_time = cur
			elif start_time is not None and cnt == t_len - k + 1:
				res.append([start_time,cur])
				start_time = None
		else:
			cnt -=1
			if i < points_len -1 and cnt == t_len - k:
				start_time = cur   
			elif start_time is not None and i == points_len -1 and cnt <= t_len - k:
				res.append([start_time,cur])
				start_time = None
		i +=1
		
	return res

if __name__ == "__main__":
	print(meeting([[[1,3],[6,7]],[[2,4]],[[2,3],[9,12]]],3))