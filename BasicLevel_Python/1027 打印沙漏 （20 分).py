N, c = input().split()

N = int(N)
def Hourglass(N, c):
    k = [0]*N
    for i in range(N):
        if i>= (N+1)/2:
            break
        k[i] = i
        k[-(i+1)] = i

    for i in range(N):
        tmp = N-k[i]*2
        print(' '*k[i]+c*tmp)

s = 0
l = [None]*45
for i in range(23)[1:]:
    s += 2*(i*2-1)
    l[2*i-1] = s-1

for k, i in enumerate(l[::-1]):
    if i is not None and N >= i:
        Hourglass(44-k, c)
        print(N-i)
        break