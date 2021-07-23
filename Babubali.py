a = int(input())
b = []
b = input().split()
for x in range(0,a):
  b[x] = int(b[x])
d = sum(b)
if(d % 2 != 0):
  print("READY FOR BATTLE")
else:
  print("NOT READY")
