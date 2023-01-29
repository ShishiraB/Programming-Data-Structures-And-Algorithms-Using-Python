def f(x):
    d=0
    y=1
    while y <= x:
        d=d+1
        y=y*3
    return(d)

print(f(2343))


# When 2343 will be passed the value of d will be 0 and y will be one
# In the first itteration y value will be 1 and x vale will be 2343 so 
# 1<=2343 true therefore the value of d will be increamented by 1 and y will be multiplied by 3
# 3<=2343     true d=2
# 9<=2343     true d=3
# 27<=2343    true d=4
# 81<=2343    true d=5
# 243<=2343   true d=6
# 729<=2343   true d=7
# 2187<=2343  true d=8
# 6561<=2343  false     return value of d
# previously value of d was 8 so the answer if f(2343) is 8