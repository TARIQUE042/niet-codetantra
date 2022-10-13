import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def sumOfHighestAndLowestElements(arr):

	array=sorted(arr)
	return array[0]+array[-1]

print(sumOfHighestAndLowestElements(arr))
