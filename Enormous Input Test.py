a,b = input().split()
a = int(a)
b = int(b)
c = []
d = []
for x in range(0,a):
  e = int(input())
  c.append(e)
  if(c[x] % b == 0):
    d.append(e)
print(len(d))
