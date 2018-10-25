#round_price
import math
import heapq
def price_round(A_list):
	
	arr = []
	sum_v = round(sum(A_list))
	
	arr_with_diff = []
	for i,a in enumerate(A_list):
		floor = math.floor(a)
		arr.append(int(floor))
		cur_gap = a - floor
		heapq.heappush(arr_with_diff,(-cur_gap,(i)))
	gap = sum_v - sum(arr)
	
	while gap > 0 :
		n_cur_gap, (cur_index)= heapq.heappop(arr_with_diff)
		gap -=1
		arr[cur_index] += 1
	return arr



if __name__ == "__main__":
	A = [1.2,2.3,3.4]

	print(price_round(A))
	print(price_round([1.2, 2.5, 3.6, 4.0]))
	print(price_round([1.4,1.8,2.3,2.9]))
	print(price_round([1.0,1.0,1.0]))