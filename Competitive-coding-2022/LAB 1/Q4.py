import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def maxSumContiguousSubArray(arr):
	
	max_so_far= -1
	max_end_here=0
	
	for i in range(0,len(arr)):
		max_end_here +=arr[i]
		if max_so_far<max_end_here:
			max_so_far=max_end_here
			
		if max_end_here<0:
			max_end_here=0
	return max_so_far

print(maxSumContiguousSubArray(arr))
