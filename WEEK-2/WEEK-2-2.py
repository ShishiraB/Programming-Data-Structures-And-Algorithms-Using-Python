x = [589,'big',397,'bash']
y = x[2:]                   #y=[397,'bash']
u = x                       #u=[589,'big',397,'bash']
w = y
w = w[0:]
w[0] = 357                  #w=[357,'bash']
x[2:3] = [487]              #x=[589,'big',487,'bash']