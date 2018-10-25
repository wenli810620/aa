import collections
import random
import copy
def findWords(board, words):
    trie = build_trie(words)

    appearence = collections.defaultdict(list)
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            search_board(board, x, y, set(), trie, [], appearence)

    visited = [[False] * len(board) for _ in xrange(len(board))]
    max_num = find_max_num(visited, appearence)
    return max_num

def build_trie(words):
    trie = {}
    for word in words:
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = word

    return trie

def search_board(board, x, y, visited, trie, path, appearence):
    if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0]) - 1:
        return

    if (x, y) in visited:
        return

    ch = board[x][y]
    if ch not in trie:
        return

    trie = trie[ch]
    if '#' in trie:
        word = trie['#']
        appearence[word].append(path + [(x, y)])

    visited.add((x, y))
    for dx, dy in zip((1, -1, 0, 0), (0, 0, 1, -1)):
        search_board(board, x+dx, y+dy, visited, trie, path + [(x, y)], appearence)


def find_max_num(visited, appearence):
    if not appearence:
        return 0

    word = random.choice(appearence.keys())
    all_appearance = appearence.pop(word)
    max_num = find_max_num(visited, copy.deepcopy(appearence))
    for sequence in all_appearance:
        if any(visited[x][y] for x, y in sequence):
            continue

        for x, y in sequence:
            visited[x][y] = True
        max_num = max(max_num, 1 + find_max_num(visited, copy.deepcopy(appearence)))
        for x, y in sequence:
            visited[x][y] = False
    return max_num


def build_sequence(board,dictionary):
    #add word into trie

    trie = {}
    for word in dictionary:
        t = trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t["#"] = "#"

    appearence = collections.defaultdict(list)
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            search_word(i,j,trie,board,"",[],appearence)
    visited = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
    print(appearence)
    return findmax(visited,appearence)


def search_word(i,j,trie,board,cur_word,path,appearence):

    if '#' in trie:
        appearence[cur_word].append(path)
        return
    if i <0 or i>=len(board) or j <0 or j >=len(board[0]) or board[i][j] not in trie or board[i][j] == '@':
        return 
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    tmp = board[i][j]
    board[i][j] = "@"
    for dir in directions:
        cur_i,cur_j = i+dir[0],j+dir[1]
        search_word(cur_i, cur_j, trie[tmp], board, cur_word+tmp, path + [(i,j)], appearence)
    board[i][j] = tmp

def findmax(visited,appearence):
    if len(appearence) == 0:
        return 0
    word = random.choice(appearence.keys())
    all_sequence = appearence.pop(word)
    max_val = findmax(visited, copy.deepcopy(appearence))

    for sequence in all_sequence:
        if any([visited[x][y] for x, y in sequence]) : continue 
        for x,y in sequence:
            visited[x][y] = True
        max_val = max(max_val,1+findmax(visited,copy.deepcopy(appearence)))
        for x,y in sequence:
            visited[x][y] = False
    return max_val
    

   






if __name__ == "__main__":
    boards = [['a','b','c'],['d','d','d'],['b','b','d']]
    words = ["abs","abc","dd","bb"]
    print(findWords(boards,words))
    print(build_sequence(boards,words))



