# calculating minm abs distance btw 2 elem and return all pair elem 
# having minm abs diff


v=[3,12,126,44,52,57,144,61,68,72,122]

def minm(V):
	V.sort()
	abs_dist=[]
	res=[]
	for i in range(len(V)-1):
		a=abs(V[i+1]-V[i])
		abs_dist.append(a)
		print("LIST->>>",abs_dist)
	print("Minimum ditance is ",min(abs_dist))
	for i in range(len(V)-1):
		if abs(V[i+1]-V[i])==min(abs_dist):
			pairs=V[i+1],V[i]
			res.append(pairs)
	print("RESULT---",res)	
minm(v)	