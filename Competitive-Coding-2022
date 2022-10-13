import sys

expr = sys.argv[1]

def evaluate(expr):
	s=expr.split(" ")
	lists=[]
	n=len(expr)
	while(len(lists)<1):
		for i in s:
			if i.isdigit():
				lists.append(int(i))
			elif(i=='+'):
				a=lists.pop()
				b=lists.pop()
				lists.append(int(a)+int(b))
			elif(i=='-'):
				a=lists.pop()
				b=lists.pop()
				lists.append(int(b)-int(a))
			elif(i=='*'):
				a=lists.pop()
				b=lists.pop()
				lists.append(a*b)
			elif(i=='/'):
				a=lists.pop()
				b=lists.pop()
				lists.append(int(b) / int(a))
	return lists.pop()

print(evaluate(expr))
