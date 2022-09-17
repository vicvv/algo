def utopianTree(n):
  h = 1
  for i in range(n):
    if i%2 == 0:
      h *=2
    else:
      h +=1
  return h

print(utopianTree(0)) # 1
print(utopianTree(1)) # 2
print(utopianTree(2)) # 3
print(utopianTree(3)) # 6
print(utopianTree(4)) # 7
print(utopianTree(5)) # 14


