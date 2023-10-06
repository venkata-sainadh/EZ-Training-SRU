def check(l,s):
    if s==0:
        return True
    if len(l)==0:
        return False
    return check(l[1:],s-l[0]) or check(l[1:],s)

l = [3,34,4,5,21,24]
l.sort()
s = 21
if s<l[0]:
    print(False)
else:
    print(check(l,s))