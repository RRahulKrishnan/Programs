x,y,z = map(int, input().split())

if x < y :
  if y < z :
    print(x,y,z,'form a sorted sequence')
  else :
    print(x,y,z,'do not form a sorted sequence')
else :
  print(x,'is not less than', y)
