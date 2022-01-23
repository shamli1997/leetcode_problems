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
#### Algorithm
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
#### Algorithm
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
#### Algorithm
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
#### Algorithm
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
#### Algorithm
 1. The resulting bit is equal to (aBit + bBit + carry) % 2. That works because the bit becomes 1 only if the sum (aBit + bBit + carry) is greater than 2. Example: 1+1+1 = 3 => 3%2 = 1
 2. Carry can be calculated as (aBit + bBit + carry) // 2 (the result of division floor rounded). Example: 1+1+1 = 3 => carry = 3//2 = 1
 3. Use negative index i here to iterate from the end (list[-1] gives the last element of the list). That allows us to have just one single index for both strings.
</details>

### [11.1022_sum_of_root_to_leaf_binary_num](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/11.1022_sum_of_root_to_leaf_binary_num.py)
###### Leetcode Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
<details><summary> Approach </summary>

#### Time Complexity: O(N)
#### Space Complexity: O(H) H:Height of the tree.
#### Algorithm
 1. sum = sum * 2 + root.val
 2. if root.left or root.right call the recursive function and return the left + right sum
 3. else return sum
</details>

### [12.701_insert_into_bst](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/12.701_insert_into_bst.py)
###### Leetcode Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
<details><summary> Approach </summary>

#### Time Complexity: O(log base 2 N)
#### Algorithm
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
#### Algorithm
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
#### Algorithm
1. we can store nodes with the same value together in a graph dictionary. With this method, when searching, we do not need to iterate the whole list to find the nodes with the same value as the next steps, but only need to ask the precomputed dictionary. However, to prevent stepping back, we need to clear the dictionary after we get to that value.


</details>

### [16.849_max_distance_to_closest_person](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/16.849_max_distance_to_closest_person.py)
###### Leetcode Link: https://leetcode.com/problems/maximize-distance-to-closest-person/
<details><summary> Approach </summary>

#### Time Complexity: O(N), where N is the length of seats.

#### Space Complexity: O(1).
#### Algorithm
1. Keep track of prev, the filled seat at or to the left of i, and future, the filled seat at or to the right of i.

2. Then at seat i, the closest person is min(i - prev, future - i), with one exception. i - prev should be considered infinite if there is no person to the left of seat i, and similarly future - i is infinite if there is no one to the right of seat i.


</details>

### [17.290_word_pattern](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/17.290_word_pattern.py)
###### Leetcode Link: https://leetcode.com/problems/word-pattern/
<details><summary> Approach </summary>

#### Time Complexity: O(N)

#### Space Complexity: O(N)
#### Algorithm
1. map the letters in the pattern with words.
2. to handle the edge case for pattern -> 'a,a' s -> 'dog,cat' compare the len(set(p)) with len(set(s))


</details>

### [18.605_can_place_flower](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/18.605_can_place_flower.py)
###### Leetcode Link: https://leetcode.com/problems/can-place-flowers/
<details><summary> Approach </summary>

#### Time Complexity: O(N)

#### Space Complexity: O(1)
#### Algorithm
1. Since the code needs to check the previous and next positions of an empty position, we have to consider the edge cases for flowerbed[0] and flowerbed[-1]. The inclusion of this flowerbed = [0] + flowerbed + [0] allows us to check these two positions.
2. Also, we have to reset the empty position to 1 (occupied) and so avoid double-counting.


</details>

### [19.142_linked_list_cycle_2](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/19.142_linked_list_cycle_2.py)
###### Leetcode Link: https://leetcode.com/problems/linked-list-cycle-ii/
<details><summary> Approach </summary>

#### Time Complexity: O(N)

#### Space Complexity: O(1)
#### Algorithm
1. take two pointers slow, fast pointing to head
2. move slow pointer by 1 and fast pointer by 2 until fast == slow
3. if fast != slow then there is no cycle return None
4. take another pointer pointing to head.
5. iterate until pointer != fast
6. return pointer


</details>

### [20.875_koko_eating_bananas](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/20.875_koko_eating_bananas.py)
###### Leetcode Link: https://leetcode.com/problems/koko-eating-bananas/
<details><summary> Approach </summary>

#### Time Complexity: O(n⋅logm)

1. The initial search space is from 11 to mm, it takes \log mlogm comparisons to reduce the search space to 1.
2. For each eating speed middlemiddle, we traverse the array and calculate the overall time Koko spends, which takes O(n) for each traversal.
3. To sum up, the time complexity is O(n log m).

#### Space Complexity: O(1)
1. For each eating speed middlemiddle, we iterate over the array and calculate the total hours Koko spends, which costs constant space.
2. Therefore, the overall space complexity is O(1).
#### Algorithm
1. Initialize the two boundaries of the binary search as left = 1left=1, right = max(piles)right=max(piles).
2. Get the middle value from left and right, that is, middle = (left + right) / 2middle=(left+right)/2, this is Koko's eating speed during this iteration.
3. Iterate over the piles and check if Koko can eat all the piles within hh hours given this eating speed of middlemiddle.
4. If Koko can finish all the piles within h hours, set right equal to middle signifying that all speeds greater than middle are workable but less desirable by Koko. Otherwise, set left equal to middle +1 signifying that all speeds less than or equal to middle are not workable.
5. Repeat the steps 2, 3, and 4 until the two boundaries overlap, i.e., left == right, which means that we have found the minimum speed by which Koko could finish eating all the piles within h hours. We can return either left or right as the answer.


</details>

### [21.134_gas_station](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/21.134_gas_station.py)
###### Leetcode Link: https://leetcode.com/problems/gas-station/
<details><summary> Approach </summary>

#### Time Complexity: O(n)
#### Space Complexity: O(1)
#### Algorithm
1. Initialize the tank, start, shortage  to 0
2. Iterate over gas with index, fill in the tank tank += gas[index]
3. go on to the next gas station with current gas in tank if tank >= cost[index]: tank -= cost[index]
4. else we dont have enough gas to move to next station
5. add that to shortage shortage += cost[index] - tank
6. move to next station start = index + 1, tank = 0
7. if start == len(gas) or tank < shortage : return -1> start == len(gas) then single trip is not finished if tank < shortage we won't be able to move forward
8. finally return start value


</details>

### [22.1510_stone_game_4](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/22.1510.stone_game_4.py)
###### Leetcode Link: https://leetcode.com/problems/stone-game-iv/
<details><summary> Approach </summary>

#### Time Complexity: O(n sqrt n)
#### Space Complexity: O(n)
#### Algorithm
1. use lru_cache
2. iterate over for loop starting from 1 to the sqrt  of given num + 1(to include the number itself)
3. We need to look for all the possibilities for ex. for n=10 we need to look for 1,4,9
4. recursively call the function giving the number as current number - x value(perfect square) (n - (x*x))
5. if n==0; return False
6. if not recr_fun(n-(x*x)):return True


</details>

### [23.1291_sequential_digits](https://github.com/shamli1997/leetcode_problems/blob/main/Leetcode_Problems/January/23.1291_sequential_digits.py)
###### Leetcode Link: https://leetcode.com/problems/sequential-digits/
<details><summary> Approach </summary>

#### Time Complexity: O(1) because low & high are in range of 10^2 <= l,h <= 10^9 and it is constant
#### Space Complexity: O(1)
#### Algorithm
1. count the number of digits in lower and higher bounds
2. iterate over the for loop in range(lower_bound_digits, higher_bound_digits + 1)
3. iterate over the for loop in range(0,10 - lowee-bound_digit)
4. get the substring from (j to j+i)
5. if num >= low and num <= high: result.append(num)
6. return result


</details>
