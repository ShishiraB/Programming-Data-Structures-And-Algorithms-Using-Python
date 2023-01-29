def g(m,n):
    res = 0
    while m >= n:
        res = res+1
        m = m-n
    return(res)

print(g(92,7))

#until what value the multiple of 13 will be less than 92 the answer is 7
#since 13*7=91 therefore the max n value is 7