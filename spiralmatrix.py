def spiralmatrix(mat,row,col):
    top=0
    bottom=row-1
    left=0
    right=col-1
    dir=0
    res=[]
    while (top<=bottom and left<=right):
        if dir==0:
            for i in range(left,right+1):
              res.append(mat[top][i])
            top=top+1
        elif dir==1:
            for i in range(top,bottom+1):
                res.append(mat[i][right])
            right-=1
        elif dir==2:
            for i in range(right,left-1,-1):
                res.append(mat[bottom][i])
            bottom-=1
        elif dir==3:
            for i in range(bottom,top-1,-1):
                res.append(mat[i][left])
            left+=1
        dir=(dir+1)%4
    return res
row=int(input())
col=int(input())
mat=[]
for i in range(row):
    a=[]
   # a=list(map(int,input().split())) if it is used, the below two lines are no need only mat.append(a) is necessary
    for j in range(col,col+1):#it is only need to enter elements digit by digit
        a.append(int,input())
    mat.append(a)
print(spiralmatrix(mat,row,col))              