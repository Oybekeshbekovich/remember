# MASALALAR YECHIMI
# 1
# a, b = list(map(int, input().split()))
# print(a + b)
# import math

# 2
# n = int(input())
# if n >= 1:
#     arr = range(1, n + 1)
# else:
#     arr = range(n, 2)
# print(sum(arr))

# 3
# a=int(input())
# print(a*a)

# 4
# def guess_number(first_digit_of_result):
#     A = first_digit_of_result
#     B = 9
#     C = 9 - A
#     guessed_number = int(f"{A}{B}{C}")
#     return guessed_number
# first_digit = int(input())
# result = guess_number(first_digit)
# print(result)

# 5
# t=int(input())
# a=list(map(int, input().split()))
# list1=[]
# list2=[]
# for i in a:
#     if i%2==0:
#         list1.append(i)
#     else:
#         list2.append(i)
# for i in list2:
#     print(i,end=" ")
# print("")
# for i in list1:
#     print(i,end=" ")
# print("")
# if len(list1)>=len(list2):
#     print("YES")
# else:
#     print("NO")

# 6
# n = input()
# def ot_yurishini_tekshir(kiritish):
#     if len(kiritish) != 5 or kiritish[2] != '-':
#         return "ERROR"
#     x1, y1, x2, y2 = kiritish[0], kiritish[1], kiritish[3], kiritish[4]
#
#     if x1 not in 'ABCDEFGH' or x2 not in 'ABCDEFGH':
#         return "ERROR"
#     if y1 not in '12345678' or y2 not in '12345678':
#         return "ERROR"
#     col1 = ord(x1) - ord('A') + 1
#     row1 = int(y1)
#     col2 = ord(x2) - ord('A') + 1
#     row2 = int(y2)
#
#     dx = abs(col1 - col2)
#     dy = abs(row1 - row2)
#
#     if (dx, dy) in [(2, 1), (1, 2)]:
#         return "YES"
#     else:
#         return "NO"
# print(ot_yurishini_tekshir(n))

# 7


# 8
# a,b,c=list(map(int,input().split()))
# if a*b==c:
#     print("YES")
# else:
#     print("NO")


# 21
# a,b,c=map(int,input().split())
# max_salary=max(a,b,c)
# min_salary=min(a,b,c)
# print(max_salary-min_salary)

# 25
# a=int(input())
# b=int(input())
# if a>b:
#     print(">")
# elif a<b:
#     print("<")
# else:
#     print("=")

# 33
# g, l = map(int, input().split())
# n = g + l - 1
# print(n - g, n - l)

# 61
# a_total
# b_total
# for _ in range(4):
#     a,b=map(int,input().split())
#     a_total+=a
#     b_total+=b
# if a_total>b_total:
#     print(1)
# elif a_total<b_total:
#     print(2)
# else:
#     print("DRAW")

# 35
# k=int(input())
# for _ in range(k):
#     n,m=map(int,input().split())
#     d=19*m+((n+239)*(n+366))//2
#     print(d)

# 43
# a=input()
# b=a.split('1')
# max_lenght=max(len(c) for c in b)
# print(max_lenght)

# 81
# t=int(input())
# a=list(map(int,input().split()))
# print(min(a),max(a))

# 692
# n = int(input())
# if n > 0 and (n & (n - 1)) == 0:
#     print("YES")
# else:
#     print("NO")


# 66
# list1="qwertyuiopasdfghjklzxcvbnm"
# a=input()
# x=list1.index(a)
# if a=="m":
#     print(list1[0])
# else:
#     print(list1[x+1])

# 893
# n=int(input())
# if 3<=n:
#     result=n*(n-1)*(n-2)
#     print(result)
# elif n==2:
#     print(2)
# else:
#     print(1)

# a,b=map(int,input().split())
# result=(a*(a+1)/2)*(b*(b+1)/2)
# print(result)

# n=int(input())
# print(2**n)

# def all_sum(N):
#     all = 0
#     for i in range(10 ** N):
#         nums = list(map(int, str(i).zfill(N)))
#         if 0 in nums:
#             continue
#         p = 1
#         for r in nums:
#             p *= r
#         all += p
#     return all
# N = input()
# print(all_sum(N))


# 267
# N,x,y=map(int,input().split())
# def minimal_vaqt(N, x, y):
#     if N == 1:
#         return min(x, y)
#     eng_tezyozuv = min(x, y)
#     chap = 0
#     ong = (N - 1) * max(x, y)
#     while chap < ong:
#         o_rta = (chap + ong) // 2
#         nusxalar = (o_rta // x) + (o_rta // y)
#         if nusxalar >= N - 1:
#             ong = o_rta
#         else:
#             chap = o_rta + 1
#     return chap + eng_tezyozuv
# print(minimal_vaqt(N,x,y))

# 523
# def minimal_max_tom_hajmi(n, sahifalar, k):
#     def mumkinmi(max_hajm):
#         jami = 0
#         tomlar = 1
#         for sahifa in sahifalar:
#             if jami + sahifa <= max_hajm:
#                 jami += sahifa
#             else:
#                 tomlar += 1
#                 jami = sahifa
#         return tomlar <= k
#
#     chap = max(sahifalar)
#     ong = sum(sahifalar)
#     while chap < ong:
#         o_rta = (chap + ong) // 2
#         if mumkinmi(o_rta):
#             ong = o_rta
#         else:
#             chap = o_rta + 1
#     return chap
#
#
# n = int(input())
# sahifalar = list(map(int, input().split()))
# k = int(input())
# print(minimal_max_tom_hajmi(n, sahifalar, k))

# 712
# def minimal_kvadrat_tomoni(w, h, n):
#     chap = 0
#     ong = max(w, h) * n
#
#     while chap < ong:
#         s = (chap + ong) // 2
#         joylashgan = (s // w) * (s // h)
#         if joylashgan >= n:
#             ong = s
#         else:
#             chap = s + 1
#
#     return chap
#
#
# w, h, n = map(int, input().split())
# print(minimal_kvadrat_tomoni(w, h, n))

# 149
# a=int(input())
# b=list(map(int,input().split()))
# if len(b)!=a:
#     print(0)
# else:
#     reversed_int=b[::-1]
#     print(*reversed_int)

# a,b,c=map(int,input().split())
# print(a*b*c*2)

# 68
# start_place = input().strip()
# x = int(input())
# step = 0
# trip = x
# while True:
#     if trip == 0:
#         if start_place == "Home":
#             if step % 2 == 0:
#                 print("Yes")
#                 break
#         elif start_place == "School":
#             if step % 2 == 1:
#                 print("Yes")
#                 break
#         trip = x
#     trip -= 1
#     step += 1
#     if step > 2 * x:
#         print("No")
#         break

# 106
# N = int(input())
# tails = 0
# heads = 0
# for _ in range(N):
#     coin = int(input())
#     if coin == 1:
#         tails += 1
#     else:
#         heads += 1
# print(min(tails, heads))

# 539
# N = int(input())
# if N == 1:
#     print(0)
# elif N % 2 == 0:
#     print(N // 2)
# else:
#     print(N)


# e = 2.7182818284590452353602875
# n=int(input())
# print(round(e/(10**n)))
# E = "2.7182818284590452353602875"
# n = int(input())
# if n == 0:
#     print(3)
# else:
#     print(E[:2+n])

# n=int(input())
# max_age=-1
# index_of_oldest=0
# for i in range(1,n+1):
#     v,s=map(int,input().split())
#     if s==1:
#         if v>max_age:
#             max_age=v
#             index_of_oldest = i
# print(index_of_oldest)


# import sys
# import math
#
#
# def lcm(a: int, b: int) -> int:
#     if a == 0 and b == 0:
#         return 0
#     return abs(a // math.gcd(a, b) * b)
#
#
# if __name__ == "__main__":
#     try:
#         a, b = map(int, input().split())
#     except Exception as e:
#         print()
#         sys.exit(1)
#     print(lcm(a, b))

n=int(input())
total=0
for i in range(1,n+1):
    if n%i==0:
        total+=i
print(total)