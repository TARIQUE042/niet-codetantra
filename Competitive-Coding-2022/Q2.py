import sys

expr = sys.argv[1]

def evaluate(expr):
	lists=[]
	s=expr.split(" ")
	for i in s[::-1]:
		if i.isdigit():
			lists.append(int(i))
		else:
			a=lists.pop()
			b=lists.pop()
		if i=='+':
			lists.append((a)+(b))
		elif i=='*':
			lists.append((a)*(b))
		elif i=='/':
			lists.append((a)/(b))
		elif i=='-':
			lists.append((a)-(b))
	return int(lists.pop())

print(evaluate(expr))
