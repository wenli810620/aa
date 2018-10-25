#water_drop
'''
++        +
++www+    ++
+++w+++www++
++++++++w+++
++++++++++++
0123456789'''

#heights, total water, where to drop

def pour_water(heights,location,water):
	waters = [0]*len(heights)
	water_to_pour = None
	while water > 0:
		left = location -1
		while left >=0:
			if heights[left] + waters[left] > heights[left+1] + waters[left+1]:
				break
			left -=1
		if heights[left+1] + waters[left+1] < heights[location] + waters[location]:
			waters[left+1] +=1
			water -=1
			left +=1
			continue 

		right = location + 1
		while right < len(heights):
			if heights[right] + waters[right] > heights[right-1] + heights[right-1]:
				break   
			right +=1

		if heights[right-1] + waters[right-1] < heights[location] + waters[location]:
			waters[right-1] += 1
			water -=1
			right -=1
			continue

		waters[location] +=1
		water -=1
	print_m(heights,waters)

def print_m(heights,waters):
	n = len(heights)
	maxh = float('-inf')
	for i in xrange(n):
		maxh = max(maxh,heights[i]+waters[i])
	for height in xrange(maxh,-1,-1):
		for i in xrange(n):
			if height <= heights[i]:
				print("+")
			elif height > heights[i] and height <= heights[i] + waters[i]:
				print("w")
			else:
				print(" ")

def pour_water_2(terrains, location, water):
    
    waters = [0] * len(terrains)
    flag = False
    while water > 0:
    	if flag == False:
    		index = location
        	for i in xrange(index-1,-1,-1):
        		if terrains[i] + waters[i] > terrains[index] + waters[index]:
        			break
            	elif terrains[i] + waters[i] < terrains[index] + waters[index]:
            		index = i
                    
        	if index != location and index != 0:
            	waters[index] += 1
            	water -=1
            	continue

        	elif index == 0:
        		flag = True
        index = location

        for i in xrange(location,len(terrains)):
            if terrains[i] + waters[i] > terrains[index] + waters[index]:
                break
            elif terrains[i] + waters[i] < terrains[index] + waters[index]:
                index = i

       	waters[index] +=1
       	water -=1

    max_height = max(terrains)
    for height in xrange(max_height,0,-1):
    	cur = []
    	for i in xrange(len(terrains)):
    		if height <= terrains[i]:
    			cur += ["+"]
    		elif terrains[i] < height <= terrains[i] + waters[i]:
    			cur +=["w"]
    		else:
    			cur.append(" ")
        print("".join(cur))
    
    return 
        

if __name__ == "__main__":
	#print(pour_water_2([5,5,3,2,3,4,3,4,1,2,5,4],5,8))

	print(pour_water_2([2,3,4,5,7,9,7,5,3,2],5,6))
	#print(pour_water_2([0,1,0,2,1,0,1,3,2,1,2,1],8,5))
	