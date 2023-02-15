#Question-1

def primepartition(m):
    if m <= 2:
        return False
    for i in range(2, m):
        if is_prime(i) and is_prime(m-i):
            return True
    return False
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Question-2

def matched(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
    return not stack


#Question-3

def rotatelist(l, k):
    if k <= 0:
        return l
    k = k % len(l)
    return l[k:] + l[:k]
