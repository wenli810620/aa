import collections
#Minimum Vertices to Traverse Directed Graph
#Given a directed graph, represented in a two dimensional array, output a list of points that can be used to traverse every points with the least number of visited vertices.

#traverse_graph_with_mini_vertice
'''def traverse_method(graph):
	oub = collections.defaultdict(list)
	inb = collections.defaultdict(int)
    nodes = set()
	for i in xrange(len(graph)):
		for j in xrange(len(graph[0])):
			if graph[i][j] == 1:
				oub[i].append(j)
				inb[j] +=1
				node.add(i)
				node.add(j)
				
    #cnt 
    res = []
    visited = set()
    for node in nodes:
    	if node not in visited and inb[node] == 0:
    		queue = []
    		queue.append(node)
    		visited.add(node)
    		res.append(node)
    		while queue:
    			cur = queue.pop(0)
    			for nxt in oub[cur]:
    				if nxt not in visited:
    					queue.append(nxt)
    					visited.add(nxt)
    return res'''

def min_node(matrix):
    result = []
    oub = collections.defaultdict(list)
    inb = collections.defaultdict(int)
    record = set()
    node = set()
    edges = []
    for i in xrange(len(matrix)):
        record.add(i)
        node.add(i)
        for j in xrange(len(matrix[0])):
            record.add(j)
            node.add(j)
            if matrix[i][j] == 1:
                edges.append([i,j])
    print(edges)
    for x,y in edges:
        oub[x].append(y)
        inb[y] +=1
    queue = []
    for n in node:
        if inb[n] == 0:
            result.append(n)
            queue.append(n)
            record.remove(n)

    while queue :
        cur = queue.pop(0)
        for nxt in oub[cur]:
            if nxt in record:
                queue.append(nxt)
                record.remove(nxt)
    
    for r in record:
        queue.append(r)
    while record:
        cur = queue.pop(0)
        result.append(cur)
        record.remove(cur)
        for nxt in oub[cur]:
            if nxt in record:
                queue.append(nxt)
                record.remove(nxt)
    return result

#sample method

'''def minVertices(edges):
    p = []

    def find(i):
        while i != p[i]:
            p[i] = p[p[i]]
            i = p[i]
        return i


    def union(x, y):
        px = find(x)
        py = find(y)
        p[py] = px

    for x, y in edges:
        if x not in p and y not in p:
            p[x] = x
            p[y] = y
            union(x, y)
        elif x in p and y not in p:
            p[y] = p[x]
        elif y in p and x not in p:
            p[x] = p[y]
        else:
            union(x, y)

    res = set()
    for x, y in edges:
        res.add(find(x))
        res.add(find(y))

    return list(res)'''


if __name__ == "__main__":

    
    matrix = [[0,1],[1,0],[3,2],[3,1],[2,1]]
    matrix1 = [[1,2],[2,3],[3,2],[4,3]]
    matrix2 = [[1,2],[2,1]]
    matrix3 = [[2,9],[3,3],[3,5],[3,7],[4,8],[5,8],[6,6],[7,4],[8,7],[9,3],[9,6]]
    matrix4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0 ,0, 0, 0, 0, 0, 0, 1], 
               [0, 0, 0, 1, 0, 1, 0, 1, 0, 0], 
               [0, 0, 0, 0, 0, 0 ,0, 0, 1, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0 ,0], 
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
               [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]]
  
    print(min_node(matrix3))
	
			

