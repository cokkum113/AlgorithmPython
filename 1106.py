import sys
input = sys.stdin.readline

#재귀로 푸는 법 알고 싶습니다. 최소일때랑 비교해서 백트래킹으로 풀 수 있을 거 같습니당....
c, n = map(int, input().split())

guestlist = []
for i in range(n):
    guest = list(map(int, input().split()))
    guestlist.append(guest)

dp = [10**9] * (c + 100)
#최솟값이 원하는 인원수를 넘어갔을 때 가질 수 있기 때문에 
dp[0] = 0

guestlist.sort(key=lambda x : x[0])

for cost, guest in guestlist:
    for i in range(guest, c + 100):
        dp[i] = min(dp[i], dp[i - guest] + cost)

print(min(dp[c:]))


