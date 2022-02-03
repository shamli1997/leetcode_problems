# February Problems

### [1.121_best_time_to_buy_sell_stock](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/1.121_best_time_to_buy_sell_stock.py)
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

### [2.438_find_all_anagrams_in_str](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/2.438_find_all_anagrams_in_str.py)
###### Leetcode Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

<details><summary>Approach</summary>

##### TC: O(N)
##### SC: O(1)
 1. Initialize pattern dictionary dict_p hashmap using collenctions.counter(p), dict_s = {}, start = 0
 2. iterate from 1 to len(s)
 3. if s[end] in the dict_s add 1 as value else increment by 1
 4. check if dict_s == dict_p: result.append(start)
 5. if (end - start + 1) >= len(p):if dic_s[s[start]] > 1:decrement the val else delete dic_s[s[start]
 6. increment start by 1
 7. return result

</details>

### [3.454_4_sum_2](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/3.454_4_sum_2.py)
###### Leetcode Link: https://leetcode.com/problems/4sum-ii/

<details><summary>Approach</summary>

##### TC: O(N*N)
##### SC: O(N*N)
 1. Initialize 2 dicts d1 d2
 2. iterate over nums1, nums2.
    1. insert num1+num2 frequency in d1
 3. Iterate over nums3, nums4
    1. insert num3+num4 frequency in d1
 4. Iterate over d1.keys()
    1. if -key in d2.keys:
        1. ans += d1[key] * d2[-key]
 5. return ans


</details>