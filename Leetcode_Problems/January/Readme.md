# January Problems

### 4.1009 Complement of base 10 integer (https://leetcode.com/problems/complement-of-base-10-integer/)
<details><summary> Approach </summary>

##### Create a mask and substract the given number.
</details>

### 5.131 Palindrome Partitioning (https://leetcode.com/problems/palindrome-partitioning/)
<details><summary> Approach </summary>

##### Use dfs to find all the substrings of the given string.
</details>

### 6.1094 Car Pooling (https://leetcode.com/problems/car-pooling/)
<details><summary> Approach </summary>

#### Time Complexity: O(n) AND Space Complexity: o(max(n,1001)).
##### 1.Create capacity array of 1001 filled with 0.
##### 2.Increment the capacityArray by trip when passenger onboards.
##### 3.Decrement the capacityArray by trip when passenger departs.
##### 4.Loop over capacityArray and decrement the passenger from given capacity.
##### 5.Return false if capacity < passenger present in the capacity_array.
</details>

### 7.382. Linked List Random Node (https://leetcode.com/problems/linked-list-random-node/)
<details><summary> Approach </summary>

#### Time Complexity: O(n) AND Space Complexity: O(1).
##### 1.Chosen value = 0 and scope = 1
##### 2.Loop through the Linked list
##### 3.if random_value < 1/scope then chosen_value = current_value of LL.
##### 4.Increment the scope by 1 and move current to next.

</details>

### 8.1463. Cherry Pickup II(https://leetcode.com/problems/cherry-pickup-ii/)
<details><summary> Approach </summary>

#### Time Complexity: O(MN^2) AND Space Complexity: O(MN^2).
##### 1.Define a dp function that takes three integers row, col1, and col2 as input.

##### 2.(row, col1) represents the location of robot1, and (row, col2) represents the location of robot2.

##### 3.The dp function returns the maximum cherries we can pick if robot1 starts at (row, col1) and robot2 starts at (row, col2).

##### 4.In the dp function:

###### 1.Collect the cherry at (row, col1) and (row, col2). Do not double count if col1 == col2.

###### 2.If we do not reach the last row, we need to add the maximum cherries we can pick in the future.

###### 3.The maximum cherries we can pick in the future is the maximum of dp(row+1, new_col1, new_col2), where new_col1 can be col1, col1+1, or col1-1, and new_col2 can be col2, col2+1, or col2-1.

###### 4.Return the total cherries we can pick.

##### 5.Finally, return dp(row=0, col1=0, col2=last_column) in the main function
</details>