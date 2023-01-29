def mys(m):
    if m == 1:
        return(1)
    else:
        return(m*mys(m-1))

print(mys(3))

#for all non -ve ,non zero integer the function displays factorial of given number