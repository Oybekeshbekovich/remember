a=int(input())
sum=0
if a<0:
    for i in range(0,a-1,-1):
        sum+=i
        print(sum)