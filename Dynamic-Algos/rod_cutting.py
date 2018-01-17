import sys
# the optimal solution follows the recurrence: r_n = MAX_i (p_i + r_{n-i})



#top down memoized
def top_memoized_rod(costs):
    def top_memoized_rod_help(costs,memoized_array,n):
        if memoized_array[n] >= 0:
            return memoized_array[n]
        elif n == 0:
            cost_at_layer = 0
        else:
            cost_at_layer = -sys.float_info.min
            for i in range(1,n + 1):
                cost_at_layer = max(cost_at_layer, costs[i] + top_memoized_rod_help(costs,memoized_array,n-i))

        memoized_array[n] = cost_at_layer
        return cost_at_layer
    return top_memoized_rod_help(costs,[-sys.float_info.min] * (len(costs) + 1), len(costs))


def bottom_memoized_rod(costs):
    memo = [0] * (len(costs) + 1 )
    for j in range(1,len(costs) + 1):
        q = -sys.float_info.min
        for i in range(1,j + 1):
            q = max(q,costs[i] + memo[j-i])
        memo[j] = q
    return memo[-1]

if __name__ == "__main__":
    cost_table = {1: 1, 2: 5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}
    print(bottom_memoized_rod(cost_table))

