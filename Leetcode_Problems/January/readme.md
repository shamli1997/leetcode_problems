# January Problems

### [4.1009 Complement of base 10 integer](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/4.1009_complement_of_base_10_int.py)
###### Leetcode Link: https://leetcode.com/problems/complement-of-base-10-integer/
<details><summary> Approach </summary>

 1. Create a mask and substract the given number.
</details>

### [5.131 Palindrome Partitioning](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/5.131_palindrome_partitioning.py)
###### Leetcode Link: https://leetcode.com/problems/palindrome-partitioning/
<details><summary> Approach </summary>

 1. Use dfs to find all the substrings of the given string.
</details>

### [6.1094 Car Pooling](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/6.1094_car_pooling.py)
###### Leetcode Link: https://leetcode.com/problems/car-pooling/
<details><summary> Approach </summary>

#### Time Complexity: O(n)
#### Space Complexity: o(max(n,1001)).
 1. Create capacity array of 1001 filled with 0.
 2. Increment the capacityArray by trip when passenger onboards.
 3. Decrement the capacityArray by trip when passenger departs.
 4. Loop over capacityArray and decrement the passenger from given capacity.
 5. Return false if capacity < passenger present in the capacity_array.
</details>

### [7.382. Linked List Random Node](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/7.382_linked_list_random_node.py)
###### Leetcode Link: https://leetcode.com/problems/linked-list-random-node/
<details><summary> Approach </summary>

#### Time Complexity: O(n)
#### Space Complexity: O(1).
 1. Chosen value = 0 and scope = 1
 2. Loop through the Linked list
 3. if random_value < 1/scope then chosen_value = current_value of LL.
 4. Increment the scope by 1 and move current to next.

</details>

### [8.1463. Cherry Pickup II](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/8.1463_cherry_pick_up_2.py)
###### Leetcode Link: https://leetcode.com/problems/cherry-pickup-ii/
<details><summary> Approach </summary>

#### Time Complexity: O(MN^2)
#### Space Complexity: O(MN^2).
 1. Define a dp function that takes three integers row, col1, and col2 as input.
 2. (row, col1) represents the location of robot1, and (row, col2) represents the location of robot2.
 3. The dp function returns the maximum cherries we can pick if robot1 starts at (row, col1) and robot2 starts at (row, col2).
 4. In the dp function:
    1. Collect the cherry at (row, col1) and (row, col2). Do not double count if col1 == col2.
    2. If we do not reach the last row, we need to add the maximum cherries we can pick in the future.
    3. The maximum cherries we can pick in the future is the maximum of dp(row+1, new_col1, new_col2), where new_col1 can be col1, col1+1, or col1-1, and new_col2 can be col2, col2+1, or col2-1.
    4. Return the total cherries we can pick.
 5. Finally, return dp(row=0, col1=0, col2=last_column) in the main function
</details>

### [9.1049_robot_bounded_in_circle](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/9.1049_robot_bounded_in_circle.py)
###### Leetcode Link: https://leetcode.com/problems/robot-bounded-in-circle/submissions/
<details><summary> Approach </summary>

#### Time Complexity: O(N)
#### Space Complexity: O(1).
 1. Set direction:di(0,1) as it is moving straight towards north.
 2. Keep starting position at (0,0).
 3. Iterate through instruction string
 4. if "G": Go straight that means add x+di[0],y+di[1]
 5. if "L": Change direction: di(-di[1],di[0])
 6. if "R": Change direction: di(di[1],-di[0])
 7. Check if x,y==0,0 or di!=(0,1) #no circle found if di is (0,1)
</details>

### [10.67_add_binary](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/10.67_add_binary.py)
###### Leetcode Link: https://leetcode.com/problems/add-binary/
<details><summary> Approach </summary>

#### Time Complexity: O(N)
#### Space Complexity: O(1).
 1. The resulting bit is equal to (aBit + bBit + carry) % 2. That works because the bit becomes 1 only if the sum (aBit + bBit + carry) is greater than 2. Example: 1+1+1 = 3 => 3%2 = 1
 2. Carry can be calculated as (aBit + bBit + carry) // 2 (the result of division floor rounded). Example: 1+1+1 = 3 => carry = 3//2 = 1
 3. Use negative index i here to iterate from the end (list[-1] gives the last element of the list). That allows us to have just one single index for both strings.
</details>

### [11.1022_sum_of_root_to_leaf_binary_num](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/11.1022_sum_of_root_to_leaf_binary_num.py)
###### Leetcode Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
<details><summary> Approach </summary>

#### Time Complexity: O(N)
#### Space Complexity: O(H) H:Height of the tree.
 1. sum = sum * 2 + root.val
 2. if root.left or root.right call the recursive function and return the left + right sum
 3. else return sum
</details>

### [12.701_insert_into_bst](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/12.701_insert_into_bst.py)
###### Leetcode Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
<details><summary> Approach </summary>

#### Time Complexity: O(log base 2 N)
 1. If root is empty then make node with given value and return Node
 2. if val < curr.val: 
   1. check if left node exist. True: curr = curr.left False: curr.left = TreeNode(val)
3. if val > curr.val: 
   1. check if right node exist. True: curr = curr.right False: curr.right = TreeNode(val)
4. return root
</details>

### [13.452_min_num_of_arrows_to_burst_balloons](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/13.452_min_num_of_arrows_to_burst_balloons.py)
###### Leetcode Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
<details><summary> Approach </summary>

#### Time Complexity: O(N log N)
 1. Sort the List according to 2nd element
 2. check for overlapping interval and increment the arrows and update ending point of the interval.
</details>

### [14.8_string_to_int_atoi](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/14.8_string_to_int_atoi.py)
###### Leetcode Link: https://leetcode.com/problems/string-to-integer-atoi/
<details><summary> Approach </summary>

#### Time Complexity: O(s)

![DFA: Deterministic finite automaton](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/atoi.PNG?raw=true)

</details>

### [15.1345_jump_game_4](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/15.1345_jump_game_4.py)
###### Leetcode Link: https://leetcode.com/problems/jump-game-iv/
<details><summary> Approach </summary>

#### Time complexity: O(N) since we will visit every node at most once.

#### Space complexity: O(N) since it needs curs and nex to store nodes.

1. we can store nodes with the same value together in a graph dictionary. With this method, when searching, we do not need to iterate the whole list to find the nodes with the same value as the next steps, but only need to ask the precomputed dictionary. However, to prevent stepping back, we need to clear the dictionary after we get to that value.


</details>