l=[1,2,3,3,4,5,55,5]
numbers={}
for i in l:
	numbers[i]=i*i
print(numbers)


l=[2,2,3,34,3,4,44,4,4,44,4,6,6,6]# removing duplicat elements
s={}
for i in set(l):
	s[i]=i*i
print(s)
