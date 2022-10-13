import sys

treeStr = sys.argv[1]
n = int(sys.argv[2])

def binarySearchTreeTraversal(treeStr, n):
	a=treeStr.split(' ')
	ar=[]
	def inorder(i):
		left=2*i+1
		right=2*i+2
		if i<len(a):
			inorder(left)
			if a[i]=='-':
				pass
			else:
				ar.append(a[i])
			inorder(right)
	inorder(0)
	return ar[n-1]

print(binarySearchTreeTraversal(treeStr, n))
