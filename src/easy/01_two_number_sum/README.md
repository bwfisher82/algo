### Prompt
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

### Input
 array = [3, 5, -4, 8, 11, 1, -1, 6]
 target_sum = 10

### Output
[-1, 11] # could be in reverse order

### Optimal Complexities
* O(n) time
* O(n) space
* n is the length of the input array