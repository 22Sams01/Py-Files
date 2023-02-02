# longest common prefix

s=str(input()).split(' ')
short=min(s)
t1=''
for i in range(len(short)):
	if s[len(s)-1][i] == short[i]:
		t1+=s[len(s)-1][i]
print("Longest Common Prefix is ->",t1)