def remdup(l):
    temp=[]
    l.reverse()
    for  i  in range(len(l)):
        if l[i] not in temp:
            temp.append(l[i])
    temp.reverse()
    return temp

def splitsum(l):
     pos=0
     neg=0
     for n in l:
         if n>0:
             pos=pos+n**2  
         else :
             neg=neg+n**3
     return([pos,neg])

def matrixflip(m, d):
    if d == 'h':
        return [row[::-1] for row in m]
    elif d == 'v':
        return m[::-1]
    else:
        return m