def averagelist(l):
	total=0
	for ele in range(0,len(l)):
		total=total+len(l)
		avg=total/len(l)
	return avg
l=[1,2,3,4,5,6,7,8,9]	
print(averagelist(l))	