# February Problems

### [1.121_best_time_to_buy_sell_stock](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/February/1.121_best_time_to_buy_sell_stock.py)
###### Leetcode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
<details><summary>Brute Force</summary>


##### TC: (N ^ 2)
##### SC: O(1)

1. Use a for loop of ‘i’ from 0 to n.
2. Use another for loop from ‘i+1’ to n.
3. If arr[j] > arr[i] , take the difference and compare  and store it in the maxProfit variable.
4. Return maxProfit.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(N)
##### SC: O(1)
 1. Initialize min_price = prices[0] and max_profit = 0
 2. iterate through the array
 3. min_price = min(price,min_price)
 4. max_profit = max(max_profit, price - min_price)
 5. return max_profit

</details>