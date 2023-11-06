"""121. Best Time to Buy and Sell Stock
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0."""
# class Solution:
#     def maxProfit(self, prices) -> int:
#         curr_max = 0
#         max = 0
#         for i in range(0,len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 if prices[i]<prices[j]:
#                     curr_max = prices[i]-prices[j]
#                     if max<curr_max:
#                         max = curr_max
#         return max
                        
class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            # Update the minimum price
            if price < min_price:
                min_price = price
            # Calculate the potential profit and update the maximum profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
                    

# Time complexity: O(n)

# Space Complexity: O(1)

# Brute force method 
# Algorithm / Intuition
"""Intuition: We can simply use 2 loops and track every transaction and maintain a variable maxPro 
to contain the max value among all transactions.

Approach: 

Use a for loop of ‘i’ from 0 to n.
Use another for loop of j from ‘i+1’ to n.
If arr[j] > arr[i] , take the difference and compare  and store it in the maxPro variable.
Return maxPro."""


        