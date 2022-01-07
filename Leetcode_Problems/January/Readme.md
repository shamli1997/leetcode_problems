# January Problems

### 4.1009 Complement of base 10 integer (https://leetcode.com/problems/complement-of-base-10-integer/)
##### Create a mask and substract the given number.

### 5.131 Palindrome Partitioning (https://leetcode.com/problems/palindrome-partitioning/)
##### Use dfs to find all the substrings of the given string.

### 6.1094 Car Pooling (https://leetcode.com/problems/car-pooling/)
#### Time Complexity: O(n) AND Space Complexity: o(max(n,1001)).
##### 1.Create capacity array of 1001 filled with 0.
##### 2.Increment the capacityArray by trip when passenger onboards.
##### 3.Decrement the capacityArray by trip when passenger departs.
##### 4.Loop over capacityArray and decrement the passenger from given capacity.
##### 5.Return false if capacity < passenger present in the capacity_array.

<details><summary>7.382. Linked List Random Node (https://leetcode.com/problems/linked-list-random-node/)</summary>
<p>
#### Time Complexity: O(n) AND Space Complexity: o(1).
##### 1.Chosen value = 0 and scope = 1
##### 2.Loop through the Linked list
##### 3.if random_value < 1/scope then chosen_value = current_value of LL.
##### 4.Increment the scope by 1 and move current to next.
</p>
</details>