str = input()
l=[]
for i in range(len(str)):
    l.append(str[i::])
# l.sort()
l=sorted(l)
print(l) # 길이순으로 정렬되나봄..
for i in range(len(l)):
    print(l[i])