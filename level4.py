# #level4 - step 3

# N=int(input())
# Narray=list(map(int, input().split()))
# max=0
# min=1000000
# for i in range(0,N):
#     num=int(input())
#     Narray.append(num)
#     if(Narray[i]>max):
#         max=Narray[i]
#     if(Narray[i]<min):
#         min=Narray[i]
# print(min,max)

# #level4 - step 4

#문제
#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

#예를 들어, 서로 다른 9개의 자연수

#3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

# 예제 입력 1 
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61
# 예제 출력 1 
# 85
# 8

# max=0
# array=[0,0,0,0,0,0,0,0,0]
# for i in range(0,9):
#     array[i]=int(input())
#     if array[i]>max:
#         max=array[i]
#         index=i
# print(max)
# print(index+1)

# Narray=list(map(int, input().split()))
# max=0
# for i in range(0,9):
#     num=int(input())
#     Narray.append(num)
#     if Narray[i]>max:
#         max=Narray[i]
#         index=i
# print(max)
# print(index+1)


# #level4 - step 5

# N, M = map(int, input().split())
# Narray=[0]*N
# Marray=[]

# for a in range(0,M):
#     Marray.clear()
#     i,j,k= map(int, input().split())
#     e=0
#     for c in range(0,N):
#         if((c>=i-1)&(c<=j-1)):
#             Marray.append(k)
#     for d in range(i-1,j):
#         Narray[d]=Marray[e]
#         e=e+1

# print(*Narray)


# #level4 - step 6

# N,M=map(int,input().split())
# Narray=[0]*N

# for c in range(0,N):
#     Narray[c]=c+1

# for a in range(0,M):
#     tmp=0
#     i,j=map(int,input().split())
#     tmp=Narray[i-1]
#     Narray[i-1]=Narray[j-1]
#     Narray[j-1]=tmp

# print(*Narray)


# #level4 - step 7

# Narray=[0]*28
# Numcheck=[0]*30
# Nonsubmit=[]

# for i in range(0,28):
#     Narray[i]=int(input())

# for j in range(0,28):
#     for k in range(0,30):
#         if Narray[j]==k+1:
#             Numcheck[k]=k+1

# for h in range(0,30):
#     if Numcheck[h]==0:
#         Nonsubmit.append(h+1)

# print(*Nonsubmit)


# #level4 - step 8

# N=0
# Rarray=[0]*10
# count=0
# final=0

# for i in range(0,10):
#     N=int(input())
#     Rarray[i]=int(N%42)


# for i in range(0,10):

#     if Rarray[i]==43:
#             continue
    
#     for j in range(i+1,10):

#         if Rarray[i]==Rarray[j]:
#             Rarray[j]=43

# for i in range(0,10):
#      if Rarray[i]==43:
#           count+=1

# final=int(len(Rarray)-count)

# print(final)


# #level4 - step 9

# N,M=map(int, input().split())
# i=0
# j=0
# len=0
# Narray=[0]*N

# for h in range(0,N):
#     Narray[h]=h+1  #12345

# for k in range(0,M):
#     i,j=map(int, input().split())   #2 4
#     len=j-i+1   # 4-2+1=3
#     Rarray=[0]*len

#     b=0
#     for l in range(0,len):
#         Rarray[l]=Narray[j-1-b]
#         b+=1

#     a=0
#     for h in range(i,j+1):
#         Narray[h-1]=Rarray[a]
#         a+=1
    
# print(*Narray)


# #level4 - step 10

# #과목개수입력
# N=int(input())

# #각과목점수입력
# Narray=list(map(int,input().split()))

# #최대점수도출
# max=0
# for i in range(0,N):
#     if Narray[i]>max:
#         max=Narray[i]

# #각점수수정 및 새평균도출
# sum=0
# newavr=0
# for i in range(0,N):
#     Narray[i]=float((Narray[i]/max)*100)
#     sum+=Narray[i]

# newavr=float(sum/N)

# print(newavr)




