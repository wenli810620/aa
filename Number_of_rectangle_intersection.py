def is_intersect(r1,r2):
	left = max(r1[0][0],r2[0][0])
	right = min(r1[1][0],r2[1][0])
	low = max(r1[0][1],r2[0][1]) 
	high = min(r1[1][1],r2[1][1]) 

	return True if right > left and high > low else False
	

def find(parent,i):
	while i != parent[i]:
		parent[i] = parent[parent[i]]
		i = parent[i]
	return i


def countIntersection(rectangles):
	parent = [i for i in xrange(len(rectangles))]
	
	num_intersection = 0
    
	for i in xrange(len(rectangles)-1):
		for j in xrange(i+1,len(rectangles)):
			
			if is_intersect(rectangles[i], rectangles[j]):
				root1 = find(parent, i)
				root2 = find(parent, j)
				if root1 != root2:
					parent[root2] = root1
					num_intersection +=1
	return num_intersection

'''def is_intersect(r1, r2):
    return r1[0][0] < r2[0][0] < r1[1][0] and r1[0][1] < r2[0][1] < r1[1][1] or \
               r1[0][0] < r2[1][0] < r1[1][0] and r1[0][1] < r2[1][1] < r1[1][1] '''

if __name__ == "__main__":
	print(countIntersection([[[0,0],[2,2]],[[1,1],[4,4]],[[1,1],[5,5]],[[1,1],[6,6]]]))












	

                                 