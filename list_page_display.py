import collections
import heapq
def pagination(host_list,per_page_num):
	page_list = []
	host_list = sorted(host_list, key = lambda x: x[2])
	queue = []
	for i in xrange(len(host_list)):
		queue.append((host_list[i][2],(host_list[i])))
	
	j = 0
	while queue:
		i = 0
		cur_set = set()
		checked = set()
		cur_page = []
		#sort the queue
		while queue and i < per_page_num:
			curscore, cur_list = queue.pop()
			if cur_list[1] in checked:
				cur_page.append(cur_list)
				i +=1
			else:
				if cur_list[0] not in cur_set:
					cur_page.append(cur_list)
					cur_set.add(cur_list[0])
					i +=1
				else:
					queue = [(curscore,cur_list)] + queue
				
			checked.add(cur_list[1])
		page_list.append(cur_page)
		j +=1
		if queue:
			queue = sorted(queue, key = lambda x: x[0])

	return page_list
def display_page(host_list, per_page_num):
	h_queue = []
	for h in host_list:
		h_list = h.split(",")
		heapq.heappush(h_queue, (-float(h_list[2]),(h_list)))
	res = []
	flag_done = False
	while h_queue:
		tmp = collections.deque([])
		cur_page = []
		visited = set()
		while len(cur_page) < per_page_num:
			if h_queue:
				curscore,(cur) = heapq.heappop(h_queue)
				if cur[0] not in visited:
					cur_page.append((",".join(cur)))
					visited.add(cur[0])
				else:
					tmp.append(cur)
			else:
				if tmp:
					cur_page.append(",".join(tmp.popleft()))
				else:
					flag_done = True
					break
		res += cur_page
		if flag_done == False:
			res += [""]
		while tmp:
			pop = tmp.pop()
			heapq.heappush(h_queue,(-float(pop[2]),(pop)))
	res = "\n".join(res)	
	return res

def display_page2(host_list, per_page_num):
	h_queue = collections.deque([])
	for h in host_list:
		h_list = h.split(",")
		h_queue.append((h_list))
	res = []
	flag_done = False
	while h_queue:
		tmp = collections.deque([])
		cur_page = []
		visited = set()
		while len(cur_page) < per_page_num:
			if h_queue:
				cur = h_queue.popleft()
				if cur[0] not in visited:
					cur_page.append((",".join(cur)))
					visited.add(cur[0])
				else:
					tmp.append(cur)
			else:
				if tmp:
					cur_page.append(",".join(tmp.popleft()))
				else:
					flag_done = True
					break
		res += cur_page
		if flag_done == False:
			res += [""]
		while tmp:
			h_queue.appendleft(tmp.pop())

	res = "\n".join(res)	
	return res

if __name__ == "__main__":
	host_list = ["1,28,310.6,SF",
	             "4,5,204.1,SF",
	             "20,7,203.2,Oakland",
	             "6,8,202.2,SF",
	             "6,10,199.1,SF", 
	             "1,16,190.4,SF", 
	             "6,29,185.2,SF", 
	             "7,20,180.1,SF",
	             "6,21,162.1,SF",
	             "2,18,161.2,SF",
	             "2,30,149.1,SF",
	             "3,76,146.2,SF", 
	             "2,14,141.1,San Jose"]
	per_page_num = 5
	res = display_page(host_list, per_page_num)
	#res2 = display_page2(host_list, per_page_num)
	print(res)
	
	#print("\n".join(res))

	

