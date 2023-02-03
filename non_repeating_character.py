
# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.
s=input()
s=[*s]
print(s)
for i in s:
    if s.count(i)==1:
        print("FIRST NON REPEATING character is ->",i)
        break
    elif s.count(i)!=1:
        print("No NON REPEATING character -> -1")
        break
    else:
        pass