x = ["sun",[17],2,"king",[3,4]] # Statement 1
y = x[0:8]                      # Statement 2
z = x                           # Statement 3
w = y                           # Statement 4
z[0] = 0                        # Statement 5
y[0] = y[0][0:3] + 'k'          # Statement 6
y[1][1:3] = [5,8]               # Statement 7
x[0] = x[0][1:3]                # Statement 8
w[4][0] = 1000                  # Statement 9
a = (x[4][1] == 4)              # Statement 10

#Here statement 8 gives error bcz we cannot add int as subscript over string 