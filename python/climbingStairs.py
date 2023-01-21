def climbStairs(n, memo = {}):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = climbStairs(n-1) + climbStairs(n-2)
    return memo[n]

print(climbStairs(10))
