from bisect import bisect_right
n = int(input())
arr = list(map(int,input().split()))
arr.sort()

for _ in range(int(input())):
    print(bisect_right(arr,int(input())))