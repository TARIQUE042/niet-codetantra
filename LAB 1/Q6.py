import sys

arr = sys.argv[1].split(',')

def lengthIndexMatch(arr):
	s=''
	k=0
	for i in arr:
		if k==len(str(i)):
			s+=str(i)
		k+=1
	if s=="":
		return "no match found"
	else:
		return s

print(lengthIndexMatch(arr))
