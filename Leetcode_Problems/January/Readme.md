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
