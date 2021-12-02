x=open("input","r").readlines()

print(sum([1 for i in range(3,len(x)) if int(x[i])>int(x[i-3])]))