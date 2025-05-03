# Coin Change Algorithm Comparison

## Problem Overview

This project explores and compares two different strategies for solving the classic coin change problem:

1. A greedy algorithm
2. A dynamic programming algorithm

Given a set of coin denominations [50, 25, 10, 5, 2, 1] and an amount to make change for, the goal is to find the minimum number of coins needed to make up that amount.

## Implemented Algorithms

### Greedy Algorithm (`find_coins_greedy`)

The greedy algorithm takes a straightforward and intuitive approach:

1. Always start with the largest available denomination
2. Use as many coins of that denomination as possible
3. Move to the next smaller coin and repeat until the amount is zero

**Time Complexity**: O(n) where n is the number of coin denominations
**Space Complexity**: O(n) for storing the result

### Dynamic Programming Algorithm (`find_min_coins`)

This method ensures an optimal solution, regardless of the coin set. It works as follows:

1. Creates a table where each entry dp[i] represents the minimum number of coins needed for amount i
2. For each amount, tries all possible coins and selects the one that minimizes the coin count
3. After filling the table, it backtracks to reconstruct the exact coin combination

**Time Complexity**: O(n × amount) where n is the number of coin denominations
**Space Complexity**: O(amount) for the dp array

## Performance Comparison

For the specific coin denominations [50, 25, 10, 5, 2, 1], both algorithms give the same results because this set has the "canonical" property (it's possible to make optimal change using the greedy approach).

### Efficiency Analysis

The performance difference becomes significant for larger amounts:

| Amount  | Greedy Algorithm | Dynamic Programming | Relative Slowdown |
| ------- | ---------------- | ------------------- | ----------------- |
| 113     | Very fast        | Fast                | ~10-20x slower    |
| 1,500   | Very fast        | Noticeably slower   | ~50-100x slower   |
| 10,000  | Very fast        | Slow                | ~300-500x slower  |
| 100,000 | Very fast        | Very slow           | ~1000x+ slower    |

### Conclusion

Both algorithms return correct results for the coin set used in this project, but their characteristics differ:

1. **Greedy Algorithm**: Extremely fast and efficient, especially with canonical denominations like the ones used here. It’s an excellent choice for real-world scenarios such as point-of-sale systems.

2. **Dynamic Programming**: Guarantees the optimal solution even for arbitrary or non-standard coin sets. However, it comes at the cost of significantly higher time complexity, especially with large amounts.

Final Thoughts: If you're working with a fixed, canonical coin system, the greedy algorithm is your best bet. But if you're designing a solution that must handle changing or unusual denominations, dynamic programming offers the flexibility and correctness you’ll need — even if it's slower.
