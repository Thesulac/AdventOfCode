data = open("input","r").readlines()

depth,hor = 0,0
aim = 0

for i in data:
  i=i.split()
  if i[0] == "up":
    depth-=int(i[1])
  elif i[0] == "down":
    depth+=int(i[1])
  else:
    hor+=int(i[1])
    aim+=int(i[1])*depth

print("depth: ", depth, "hor: ", hor, "aim: ", aim)
print("part 1: ", depth*hor)
print("part 2: ", aim * hor)