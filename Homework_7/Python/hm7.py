a = int(input('Введите количество множ А: '))

A = []
B = []
def tog(A,B):
    together = []
    num = A.intersection(B)
    for i in num:
        if (int(i) /10 ==0 and int(i) == 1) or( int(i)>= 10 and int(i)<20):
            together.append(i)
    together = set(together)
    return together

for _ in range(a):
    x = int(input())
    A.append(x)
A = set(A)
b = int(input('Введите количество множ B: ')) 
for _ in range(b):
    x = int(input())
    B.append(x)
B = set(B)
print(tog(A,B))
