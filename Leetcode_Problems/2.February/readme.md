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

### [4.525_contiguous_array](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/4.525_contiguous_array.py)
###### Leetcode Link: https://leetcode.com/problems/contiguous-array/

<details><summary>Approach</summary>

##### TC: O(N)
##### SC: O(N)
 1. Initialize total, maxlength = 0, 0 and prefix_sum={-1:0}
 2. iterate over ienumerate(nums)
      1. if num == 0: total--
      2. if num == 1: total++
      3. if total not in prefix_sum.keys(): prefix_sum[total] = index
      4. else: maxlength = max(maxlength,index - prefi_sum)
3. return maxlength



</details>

### [5.23_merge_k_sorted_linked_list](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/5.23_merge_k_sorted_linked_list.py)
###### Leetcode Link: https://leetcode.com/problems/merge-k-sorted-lists/

<details><summary>Approach</summary>

##### TC: O(N log k) where k is the number of linked lists
##### SC: O(1)
1. Pair up k lists and merge each pair.

2. After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.

3. Repeat this procedure until we get the final sorted linked list.

Thus, we'll traverse almost NN nodes per pairing and merging, and repeat this procedure about log{k} times.

 

</details>

### [6.80_remove_duplicates_from_array](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/6.80_remove_duplicates_from_array.py)
###### Leetcode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

<details><summary>Approach</summary>

##### TC: O(N) 
##### SC: O(1)
1. if len of nums < 3 return len(NUMS)
2. iterate over nums from 1 to len(nums) - 1
   1. if nums[i-1]!=nums[i+1]
      1. nums[count] = nums[i]
      2. count += 1
3. nums[count] = nums[-1]
4. return count + 1

 

</details>

### [7.389_find_the_difference](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/7.389_find_the_difference.py)
###### Leetcode Link: https://leetcode.com/problems/find-the-difference/

<details><summary>Approach</summary>

##### TC: O(N) 
##### SC: O(1)
1. initialize c = 0
2. iterate over s and xor ord(s) with c
3. iterate over t and xor ord(t) with c
4. return c

 

</details>


### [8.258_add_digits](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/8.258_add_digits.py)
###### Leetcode Link: https://leetcode.com/problems/add-digits/

<details><summary>Approach</summary>

##### TC: O(N) 
##### SC: O(1)
1. initialize res = num
2. iterate while len(str(res))>1
   1. div_num = res // 10
   2. rem = res % 10
   3. res = div_num + rem
3. return res
</details>

### [10.560_subarray_sum_equals_k](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/10.560_subarry_sum_equals_k.py)
###### Leetcode Link: https://leetcode.com/problems/subarray-sum-equals-k/

<details><summary>Approach</summary>

##### TC: O(N) 
##### SC: O(N)
1. initialize sum, count, d[0] = 0, 0 ,0
2. iterate over arr
   1. sum += arr[i]
   2. count += d.get(sum - k,0)
   3. d[sum] = d.get(sum,0) + 1
3. return count
</details>

### [11.567_permutation_in_str](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/11.567_permutation_in_str.py)
###### Leetcode Link: https://leetcode.com/problems/permutation-in-string/

<details><summary>Approach</summary>

##### TC: O(N) 
##### SC: O(N)
1. Create a window of size s1.
2. Check s2 if occurances of characters is same between s1 and s2 by sliding window from 0 to len(s2) - window_size.
</details>

### [16.24_swap_nodes_in_pair](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/2.February/16.24_swap_nodes_in_pair.py)
###### Leetcode Link: https://leetcode.com/problems/swap-nodes-in-pairs/

<details><summary>Approach</summary>

##### TC: O(N) 
##### SC: O(1)
1. Here, pre is the previous node. Since the head doesn't have a previous node, used self instead. Again, a is the current node and b is the next node.

2. To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. Instead of thinking about in what order to change them, just change all three at once.
</details>