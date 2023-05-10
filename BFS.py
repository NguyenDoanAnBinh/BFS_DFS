from sys import maxsize
 
def createStack():
    stack = []
    return stack
 
def isEmpty(stack):
    return len(stack) == 0
 
def pushf(stack, item):
    if (isEmpty(stack)):
        stack.append(item)
    else:
        stack.append(item)
        for i in range(len(stack)-1):
            stack[len(stack)-1-i]=stack[len(stack)-2-i]
        stack[0]=item

def push(stack, item):
    stack.append(item)
   
     
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)
    else:
        del stack[len(stack)-1]
        return stack
 
def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)
    return stack[len(stack) - 1]

def sort(stack):
    for i in range(len(stack)-1):
        for j in range(len(stack)-i-1):
            if (stack[j]<stack[j+1]):
                stack[j],stack[j+1]=stack[j+1],stack[j]
    return stack

def createegde(graph,a,b):
    graph[a][b]=1

def BFS(f,e,n,graph):
    scan = []
    for i in range(n):
        scan.append(-1)
    Scan(scan,n,f,e,graph)

def Scan(scan,n,f,e,graph):
    wait = createStack()
    scaned = createStack()
    check = createStack()
    pushf(wait,f)
    time=-1
    a=0
    while(isEmpty(wait)==0):
        u = peek(wait)
        pop(wait)
        if (scan[u]!=-1):
            continue
        push(scaned,u)
        if (u==e):
            a=1
            break
        time=time+1
        scan[u]=time
        for v in range(n):
            if ((graph[u][v]==1)|(graph[v][u]==1)):
                if (scan[v]==-1):
                    push(check,v)
        check = sort(check)
        for v in range(len(check)):
            pushf(wait,peek(check))
            pop(check)
    if (a==1):
        print()
        print("Ket qua thuc hien thuat toan BFS tu dinh %d la: " %f,end=" ")
        print()
        for i in scaned:
           print(i,end=" ")
        print()
    else:
        print()
        print("khong tim duoc duong di den gia tri hoac gia tri khong co")
        print()

if __name__ == "__main__":
    while(1):
        print()
        print("Chon loai nhap ma tran")
        print("1. Chon ma tran co san")
        print("2. Nhap ma tran")
        print("0. Thoat")
        i=int(input())
        print()
        if (i==0):
            break
        else:
            if ((i==1)|(i==2)):
                if (i==1):  
                    graph= [
                       [0,1,0,0,0,1,0,0,0,0],
                       [1,0,1,1,0,0,0,0,0,0],     
                       [0,1,0,0,1,0,0,0,0,0],
                       [0,1,0,0,0,0,0,0,0,0],
                       [0,0,0,1,0,0,0,0,0,0],
                       [1,0,0,0,0,0,1,0,1,0],
                       [0,0,0,0,0,1,0,1,1,0],
                       [0,0,0,0,0,0,1,0,1,1],
		               [0,0,0,0,0,1,1,1,0,0],
		               [0,0,0,0,0,0,0,1,0,0],
                    ]
                    n = len(graph[0])
                else:
                            n=int(input("nhap so dinh: "))
                            graph=[]
                            for i in range(n):
                                graph.append([])
                                for j in range(n):
                                    graph[i].append(0)
                            c=0;
                            while (c!=n):
                                while(1):
                                    b=int(input("Dinh %d lien ket voi dinh: " %c))
                                    if ((b==c)|(b>=n)):
                                        break;
                                    else:
                                        createegde(graph,c,b)
                                c=c+1
                                print()
                print("Ma tran do thi la: ")
                print()
                for i in range(n):
                    for j in range(n):
                        print(graph[i][j],end=" ")
                    print()
                print()
                while(1):
                    f=int(input("nhap dinh bat dau: "))
                    if ((f<n)&(f>=0)):
                        break;
                e=int(input("nhap dinh dich: "))
                BFS(f,e,n,graph)
            else:
                    print("Khong co muc nay!!")