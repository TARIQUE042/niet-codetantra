import sys

arr = [int(x) for x in sys.argv[1].split(',')]
s = int(sys.argv[2])

def pairsOfSum(arr, s):
	ind1=[]
	ind2=[]
	for i in range(len(arr)-1):
		for j in range(i+1,len(arr)):
			if arr[i]+arr[j]==s and i!=j:
				ind1.append(i)
				ind2.append(j)
	s=""
	for k in range(len(ind1)):
		s+="<"+str(ind1[k])+","+str(ind2[k])+">,"
	if s=="":
		return "no such pairs"
	else:
		return s[:-1]

print(pairsOfSum(arr, s))
