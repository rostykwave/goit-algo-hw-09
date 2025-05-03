import time

def find_coins_greedy(amount):
    """
    Greedy algorithm to find minimum number of coins to make change.
    
    Args:
        amount: The amount to make change for
        
    Returns:
        Dictionary with coin denominations as keys and their counts as values
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    
    return result

def find_min_coins(amount):
    """
    Dynamic programming algorithm to find minimum number of coins to make change.
    
    Args:
        amount: The amount to make change for
        
    Returns:
        Dictionary with coin denominations as keys and their counts as values
    """
    coins = [50, 25, 10, 5, 2, 1]
    
    # Initialize dp array and coin used array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [None] * (amount + 1)
    
    # Fill dp array
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    # Reconstruct the solution
    result = {}
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin
    
    return result

def compare_algorithms(amount):
    """Compare and display results of both algorithms for a given amount."""
    print(f"Finding change for {amount}:")
    
    start = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start
    print(f"Greedy Algorithm: {greedy_result}")
    print(f"Time taken: {greedy_time:.6f} seconds")
    
    start = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start
    print(f"Dynamic Programming: {dp_result}")
    print(f"Time taken: {dp_time:.6f} seconds")
    
    print(f"Dynamic Programming is {dp_time / greedy_time:.2f} times slower than Greedy for this amount")
    print()

if __name__ == "__main__":
    # Test with various amounts
    compare_algorithms(113)
    compare_algorithms(1500)
    compare_algorithms(10000)
    compare_algorithms(100000)
