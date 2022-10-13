import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def middleElementOfArray(arr):

	l=len(arr)
	if l%2==0:
		return arr[(l//2)-1]
	else:
		return arr[l//2]

print(middleElementOfArray(arr))
