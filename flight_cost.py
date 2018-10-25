#flight_cost
#-*- coding: utf-8 -*-
'''Given a flight itinerary consisting of starting city, destination city, 
and ticket price (2d list) - find the optimal price flight path to get from start to destination. 
(A variation of Dynamic Programming Shortest Path)
Output list of strings representing a page of hostings given a list of CSV strings.'''

import heapq
class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        # write your code here
        map = {}
        for start, end, cost in flights:
            if start not in map:
                map[start] = [(cost, end)]
            else:
                map[start].append((cost, end))
        if src not in map:
            return -1
        
        hq = []
        best = {}
        for cost, next_stop in map[src]:
            heapq.heappush(hq, (cost, next_stop, 0))
        
        while hq:
            cml_cost, cur_stop, level = heapq.heappop(hq)
            if cur_stop == dst:
            	return cml_cost
            if level + 1 > K:
                continue
            
            if cur_stop in map:

                for next_cost, next_stop in map[cur_stop]:
                	new_cost = cml_cost + next_cost
                	if new_cost < best.get((next_stop,level +1),float("inf")):
                    	heapq.heappush(hq, (cml_cost+next_cost, next_stop, level+1))
                    	best[(next_stop,level+1)] = new_cost
        
        return -1

#time O(E+nlogn)
#space O(n)
def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        map_d = {}
        for start,end,price in flights:
            if start not in map_d:
                map_d[start] = [(end,price)]
            else:
                map_d[start].append((end,price))
        if src not in map_d:
            return -1
        heap = []
        for end,cost in map_d[src]:
            heapq.heappush(heap,(cost,(end,0,str(src)+"->"+str(end))))
        while heap:
            curcost,(end,level,path) = heapq.heappop(heap)
            if end == dst:
                return (curcost,path)
            if map_d[end]:
                for nxt,price in map_d[end]:
                    if level+1 <= K:
                        heapq.heappush(heap,(curcost+price,(nxt,level+1,path+"->"+str(nxt))))
        return -1





if __name__ == "__main__":
	flights = ((A,B,100),(B,C,100),(A,C,500))
	print(find_path(flights))
