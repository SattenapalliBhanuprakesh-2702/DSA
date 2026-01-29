# Here’s a **professional, interview-ready breakdown** for your **Maximum Profit (Best Time to Buy & Sell Stock)** problem:


# ## **Question — Best Time to Buy and Sell Stock**

# **Problem Statement:**

# You are given an array `prices` where `prices[i]` is the price of a given stock on day `i`.

# Your task is to **compute the maximum profit** you can achieve by buying **exactly once** and selling **exactly once**.

# * You **cannot sell before you buy**.
# * If no profit is possible, return `0`.

# **Example 1:**

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price=1), sell on day 5 (price=6).

# **Example 2:**

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: Prices decrease continuously, no profit possible.

# ## **Intuition / Approach**

# 1. **Observation:**

#    * To maximize profit, we must **buy at the lowest price so far** and sell at the highest price after it.

# 2. **Algorithm (Greedy):**

#    * Initialize `min_price` as the first element.
#    * Initialize `max_profit` as `0`.
#    * Iterate through the array starting from the second element:

#      1. Calculate the potential profit if sold today: `current_profit = price - min_price`.
#      2. Update `max_profit = max(max_profit, current_profit)`.
#      3. Update `min_price = min(min_price, price)`.
#    * Return `max_profit` at the end.

# **Why it works:**

# * By tracking the **lowest price so far**, we ensure the buy always occurs before the sell.
# * Each element is processed only once → optimal.

# ## **Complexity Analysis**

# | Metric  | Complexity | Explanation                                            |
# | ------- | ---------- | ------------------------------------------------------ |
# | Time    | **O(n)**   | Single traversal of the prices array                   |
# | Space   | **O(1)**   | Only two variables (`min_price`, `max_profit`)         |
# | Optimal | ✅          | Best possible solution for single buy-sell transaction |

# ## **Test Cases**

# | Test Case           | Expected Output | Notes                        |
# | ------------------- | --------------- | ---------------------------- |
# | `[7,1,5,3,6,4]`     | 5               | Buy at 1, sell at 6          |
# | `[7,6,4,3,1]`       | 0               | No profit possible           |
# | `[1,2,3,4,5]`       | 4               | Increasing prices            |
# | `[1]`               | 0               | Single element array         |
# | `[]`                | 0               | Empty array                  |
# | `[2,2,2,2]`         | 0               | All prices equal             |
# | `[3,1,4,8,7,2,5]`   | 7               | Maximum profit in middle     |
# | `[1,1000000]`       | 999999          | Large numbers                |
# | `[1000000,1]`       | 0               | Large decreasing numbers     |
# | `[3,3,5,0,0,3,1,4]` | 4               | Multiple local minima/maxima |




def Buy_Sell(prices):
    if not prices or len(prices)<2:
        return 0
    mini_price=prices[0]
    max_profit=0
    for i in range(1,len(prices)):
        
        profit=prices[i]-mini_price
        
        max_profit=max(max_profit,profit)
        
        mini_price=min(mini_price,prices[i])
        
    return max_profit


prices=list(map(int,input("Enter array elements : ").split()))
print(f"profit id : {Buy_Sell(prices)}")