size=int(input("Enter the column size of matrix:"))
one={"rowC":0,"columnC":0,"diagonalL":0,"diagonalR":0}
zero={"rowC":0,"columnC":0,"diagonalL":0,"diagonalR":0}
matrix=list(map(int,input().split(" ")))
matrix = [list(row) for row in zip(*[iter(matrix)]*size)]
print(matrix)
dr=size-1
dl=0
s=[0,0,0,0]
for lis in matrix:
    if(sum(lis)==size):
        one["rowC"]+=1
    elif(sum(lis)==0):
        zero["rowC"]+=1
    one["diagonalR"]+=lis[dr]
    one["diagonalL"]+=lis[dl]
    zero["diagonalR"]+=lis[dr]
    zero["diagonalL"]+=lis[dl]
    dr-=1
    dl+=1
    s=[x + y for x, y in zip(s,lis)]
one["diagonalR"]//=size
one["diagonalL"]//=size
zero["diagonalR"]//=size 
zero["diagonalL"]//=size
for i in s:
    if(i==0):
        zero["columnC"]+=1
    elif(i==size):
        one["columnC"]+=1
print("Zero==>",zero,"\nOne==>",one)