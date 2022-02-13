import sys
input = sys.stdin.readline

t = int(input())

#[True, True는 앞에 0, 1 무시]

#소수를 구할 때, 에라토스테네스의 체로 구하기
def find_prime(n):
    primes = []
    nums = [True] * n
    sqr = int(n ** 0.5)
    for i in range(2, sqr + 1):
        if nums[i] == True:
            for j in range(i + i, n, i):
                # i이후 i의 배수들은 prime이 아님
                nums[j] = False
    for i in range(2, len(nums)):
        if nums[i]:
            primes.append(i)     
    return primes


for _ in range(t):
    n = int(input())
    prime_list = find_prime(n)
    min_diff = n
    
    a = len(prime_list) // 2
    prime_list.sort(reverse=True)
    
    for i in range(a + 1):
        for j in range(len(prime_list)):
            if prime_list[i] + prime_list[j] == n:
                if prime_list[i] - prime_list[j] <= min_diff and prime_list[i] - prime_list[j] >= 0:
                    min_diff = prime_list[i] - prime_list[j]
                    ans1 = prime_list[i]
                    ans2 = prime_list[j]
    print(ans2, ans1)
