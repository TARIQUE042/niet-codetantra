import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def sumOfArray(arr):

	return sum(arr)

print(sumOfArray(arr))
