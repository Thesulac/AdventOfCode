
inp=open("input","r").readlines()
print(sum([1 for i in range(1,len(inp)) if int(inp[i])>int(inp[i-1])]))
