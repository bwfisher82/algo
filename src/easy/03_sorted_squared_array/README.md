### Prompt
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order. Do not alter the input array.

### Note
Squaring a negative produces a positive such that -4^2 is 16, not -16. Online calculators may show the result as -16 because they analyze -4^2 as an expression, and PEMDAS tells us to evaluate exponents before sign. If you put (-4)^2 in the same online calculator it would produce the expected result of 16.

### Input
 array = [1, 2, 3, 5, 6, 8, 9]

### Output
 array = [1, 4, 9, 25, 36, 64, 81]

### Optimal Complexities
* O(n) time
* O(n) space
* n is the length of the input array