def swaplist(x):
	x1=x.pop(0)
	x2=x.pop(-1)
	x.insert(0,x2)
	x.append(x1)
	print(x)#return(x)
swaplist([2,3,4,5,67,8,9])	
