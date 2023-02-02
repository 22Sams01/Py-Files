# str has vowels or not -> if yes: remove

s=str(input())
s=[*s]
a=['a','e','i','o','u','A','E','I','O','U']
z=""
for i in range(len(s)):
	if s[i] not in a:
		z+=s[i]
print("Output >>",z)