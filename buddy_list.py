#buddy_list
def buddy_gen(mylist,buddy_list):
	buddy_res = []
	res = []
	for key in buddy_list:
		wish_list = buddy_list[key]
		cnt = 0
		for city in wish_list:
			if city in mylist:
				cnt +=1
        
		similarity = float(cnt) / float(len(mylist))
		if similarity >=0.5:
			buddy_res.append((similarity,key,wish_list))
	buddy_res = sorted(buddy_res,key = lambda x:x[0], reverse = True)
	return buddy_res

def get_buddy(my_list,buddy_list):
	res = []
	buddy_res = buddy_gen(my_list, buddy_list)
	for buddy in buddy_res:
		res.append(buddy[1])
	return res

def recommend(my_list,buddy_list,max_value):
	buddy_res = buddy_gen(my_list, buddy_list)
	i = 0
	res = []
	while i < max_value:
		for j in xrange(len(buddy_res)):
			cur_list = buddy_res[j][2]
			for city in cur_list:
				if city not in my_list:
					res.append(city)
					i +=1
				if i == max_value: break
	return res



    

if __name__ == "__main__":
	print(get_buddy(["a","b","c","d"],{"b1":["a","b","e","f"],"b2":["a","b","d","g"]}))
	print(recommend(["a","b","c","d"],{"b1":["a","b","e","f"],"b2":["a","b","d","g","f"]},4))






