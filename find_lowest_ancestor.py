def find_lowest_ancestor(source, p, q):
	parent = {}
    
	while p not in parent or q not in parent:
		for cur in source:
			cur_parent = cur[0]
			if cur_parent not in parent:
				parent[cur_parent] = None
			for c in cur[1:]:
				parent[c] = cur_parent
				
	ancestor = set()
	while p in parent:
		ancestor.add(p)
		p = parent[p]

	while q not in ancestor:
		q = parent[q]
	return q

if __name__ == "__main__":
	source = [["earth", "america"],["america", "south america", "north acmerica"],["north america", "canada", "us"],["canada", "ontario", "quebec", "calgary"],["us", "california"]]
	print(find_lowest_ancestor(source, "california", "calgary"))