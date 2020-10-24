class Mft: 

     

    def __init__(self, partitions): 

        self.partitions = partitions[:] 

        self.n = len(partitions) 

        self.used = [False]*self.n 

        self.result = {0:[]} 

     

    def bfa(self, p, x): 

        ind = -1 

        dist = max(partitions)-p 

        for i in range(self.n): 

            if not self.used[i] and self.partitions[i]-p>0 and self.partitions[i]-p<=dist: 

                dist = self.partitions[i]-p 

                ind = i 

        if ind != -1: 

            self.used[ind] = True 

            self.result[ind+1] = [x, p] 

        else: 

            self.result[0].append(x) 

     

    def ffa(self, p, x): 

        ind = -1 

        for i in range(self.n): 

            if not self.used[i] and self.partitions[i]-p>0: 

                ind = i 

                break 

        if ind != -1: 

            self.used[ind] = True 

            self.result[ind+1] = [x, p] 

        else: 

            self.result[0].append(x) 

     

    def wfa(self, p, x): 

        ind = -1 

        dist = 0 

        for i in range(self.n): 

            if not self.used[i] and self.partitions[i]-p>0 and self.partitions[i]-p>=dist: 

                dist = self.partitions[i]-p 

                ind = i 

        if ind != -1: 

            self.used[ind] = True 

            self.result[ind+1] = [x, p] 

        else: 

            self.result[0].append(x) 

     

    def display(self, algo): 

        print('\n'+algo+"-fit-algorithm") 

        print('sno\tpartitions\tprocess\tsize\tinternal-fragmentation') 

        for i in range(1, self.n+1): 

            if i in self.result: 

                print(i, '\t', self.partitions[i-1], '\t\t', self.result[i][0], '\t', self.result[i][1], '\t', self.partitions[i-1]-self.result[i][1]) 

            else: 

                print(i, '\t', self.partitions[i-1]) 

        if self.result[0]: 

            print('processes '+', '.join(map(str, self.result[0]))+' does not fit as there is no free space') 

  

  

size = int(input("enter the size of physical memory: ")) 

n = int(input("enter number of partitions/processes: ")) 

partitions = [int(input("enter the partition"+str(i)+" size: ")) for i in range(1,n+1)] 

best = Mft(partitions) 

first = Mft(partitions) 

worst = Mft(partitions) 

  

for x in range(1, n+1): 

    p = int(input("enter the process"+str(x)+" size: ")) 

    best.bfa(p, x) 

    first.ffa(p, x) 

    worst.wfa(p, x) 

    if input("do you want to continue(y/n): ")!='y': 

        break 

  

best.display("best") 

first.display("first") 

worst.display("worst") 