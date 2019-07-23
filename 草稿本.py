
def generator():
    count = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i == j or j ==k or i == k :
                    continue
                count+=1
                yield str(i)+str(j)+str(k),count

g=generator()
count=0
for i,k in g :
    count+=1
    if count<11:
        print(i,k)
    else:break



