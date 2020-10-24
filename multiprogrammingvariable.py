size = int(input("enter the size of physical memory: ")) 

count = 1 

result = [] 

  

while(True): 

    psize = int(input("enter the size of process"+str(count)+": ")) 

    if psize<=size: 

        result.append([psize, True]) 

    else: 

        result.append([psize, False]) 

    if input("do you want to continue(y/n): ")!='y': 

        break 

    count += 1 

    size -= psize 

  

print('\nprocess-number\tprocess-size\tpartition-size') 

for i in range(count): 

    partition = result[i][0] if result[i][1] else 'cannot fit in memory' 

    print(i, '\t\t', result[i][0], '\t\t', partition) 

     

print('\nExternal Fragmentation: ', size) 