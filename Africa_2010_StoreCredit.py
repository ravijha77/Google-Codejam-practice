result=[]
result2 = []
n= int(raw_input())
for i in range(0,n):
	max=int(raw_input())
	l=int(raw_input())
	a=list(map(int, raw_input().split()))
	if len(a)== l:
		for i in range(len(a)):
			for j in range(i+1,len(a)):
				if(a[i]+a[j] == max):
					result.append(i+1)
					result2.append(j+1)
	else:
		print("error")
for k in range(n):
	print("Case #%i : %i %i" %(k+1,result[k],result2[k]))

