import sys

treeStr = sys.argv[1]

def levelCount(treeStr):
	
	n=len(treeStr.split())
	sum=0
	i=0
	count=0
	while sum<n:
		sum+=2**i
		i+=1
		count+=1
		
	return count

print(levelCount(treeStr))
