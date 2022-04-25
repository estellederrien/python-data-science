# https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
# Python3 program to find maximum
# achievable value with a knapsack
# of weight W and multiple instances allowed.
 
# Returns the maximum value
# with knapsack of W capacity
def unboundedKnapsack(W, n, val, wt):
 
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)]
 
    ans = 0
 
    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
 
    return dp[W]
 
# Driver program
W = 30
val = [4, 2, 10,1,2]
wt = [12, 1, 4,1,2]
n = len(val)
 
print(unboundedKnapsack(W, n, val, wt))


# This code is contributed by Anant Agarwal.