#-*- coding: utf-8 -*-
#new_file 

'''Field start -> scan quoted field -> 
            -> not quote o r comma -> scan filed -> not comma'''
'''
quote
双引号
'''
def csv_parser(source_list):
	res = []
	for source in source_list:
		cur = processing2(source)
		res.append(cur)
	return "\n".join(res)
def processing2(csv_str):
	inQuote = False
	i = 0
	res = []
	sub = ""
	while i < len(csv_str):
		if inQuote:
			if csv_str[i] == "\"":
				if i+1 < len(csv_str) and csv_str[i+1] == "\"":
					sub += csv_str[i]
					i +=1
				else:
					inQuote = False
			else:
				sub += csv_str[i]
		else:
			if csv_str[i] == "\"":
				inQuote = True
			elif csv_str[i] == ",":
				res.append(sub)
				sub = ""
			else:
				sub += csv_str[i]
		i +=1
	if len(sub) > 0:
		res.append(sub)
	return "|".join(res)




def processing(csv_str):
	inQuote = False 
	i = 0
	res = []
	sub = ""
	while i < len(csv_str):

		if inQuote:
			if csv_str[i] == '\"':
				if i < len(csv_str) -1 and csv_str[i+1] == '\"':
					sub += "\""
					i +=1
				else: 
					inQuote = False
			else: 
				sub += csv_str[i]
		else:
			if csv_str[i] == '\"':
				inQuote = True
			elif csv_str[i] == ",":
				res.append(sub)
				sub = ""
			else:
				sub += csv_str[i]
				
		i +=1
	
	if len(sub)	> 0:
		res.append(sub)
	return "|".join(res)
    
	#return "\n".join(res)
    
if __name__ == "__main__":
	print(csv_parser(["John,Smith,john.smith@gmail.com,Los Angeles,1","\"Alexandra\"\"Alex\"\"\",Menendez,alex.menendez@gmail.com,Miami,1"]))
	#print(csv_parser("\"Alexandra\"\"Alex\"\"\",Menendez,alex.menendez@gmail.com,Miami,1"))
	#print(csv_parser("aa,bb,\"aa,bb\",\"aa\"\"b\"\"\""))
	#print(csv_parser())




            