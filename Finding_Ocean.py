#Finding_Ocean.py
'''Given: An array of strings where L indicates land and W indicates water, and a coordinate marking a starting point in the middle of the ocean.
Challenge: Find and mark the ocean in the map by changing appropriate Ws to Os. An ocean coordinate is defined to be the initial coordinate if a W, and
any coordinate directly adjacent to any other ocean coordinate.'''

def find_ocean(matrix,i,j): 
	m = len(matrix)
	n = len(matrix[0])
	new_color = "L"
	dfs(matrix,i,j,matrix[i][j],new_color)
	return matrix





def dfs(matrix,i,j,old_color,new_color):
	if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != old_color:
		return 
	matrix[i][j] = new_color
	directions = ((0,1),(0,-1),(1,0),(-1,0))
	for dir in directions:
		cur_i,cur_j = i+ dir[0], j + dir[1]
		dfs(matrix, cur_i, cur_j, old_color, new_color)


if __name__ == "__main__":
	matrix = [["W","W","W","L","L","L","W"], 
	          ["W","W","L","L","L","W","W"], 
	          ["W","L","L","L","L","W","W"]]
	print(find_ocean(matrix,0,1))



