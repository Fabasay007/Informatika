T = int(input())
a = []
n = 10
i = 0 
def build_b(a,t):
    b = []
    for j in range(len(a)):
        if a[j]> t:
            b.append(a[j])
    return b
while i < n:
    x = int(input())
    a.append(x)
    i+=1

print(build_b(a,T) )