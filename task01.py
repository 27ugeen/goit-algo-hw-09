import time

def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time * 1000


def find_coins_greedy(amount, coins):
    coin_count = {}
    for coin in coins:
        if amount >= coin:
            coin_count[coin] = amount // coin
            amount %= coin
    return coin_count


def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = {}
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin
    result = {}
    remaining = amount
    while remaining > 0:
        coin = coin_count[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin
    return result


greedy_coins = [50, 25, 10, 5, 2, 1]
min_coins = [1, 2, 5, 10, 25, 50]
amount = 113

print("Greedy Algorithm Result:", find_coins_greedy(amount, greedy_coins))
print("Dynamic Programming Result:", find_min_coins(amount, min_coins))
print("=" * 42)

custom_coins = [5, 25, 2, 50, 1, 10]

print("Greedy Algorithm Custom Result:", find_coins_greedy(amount, custom_coins))
print("Dynamic Programming Custom Result:", find_min_coins(amount, custom_coins))
print("=" * 42)

amounts = [10, 100, 1000, 10000, 100000]

for amount in amounts:
    print(f"Amount: {amount}")
    greedy_time = measure_execution_time(find_coins_greedy, amount, greedy_coins)
    dynamic_time = measure_execution_time(find_min_coins, amount, min_coins)
    print(f"Greedy algorithm time: {greedy_time} milliseconds")
    print(f"Dynamic algorithm time: {dynamic_time} milliseconds")
    print("=" * 42)

# //================================================================
# //=================== my_custom_func =============================

# def min_nums_of_coins(n, coins):
#     nums = [float('inf') for x in range(n+1)]
#     nums[0] = 0
#     for coin in coins:
#         for amount in range(len(nums)):
#             if coin <= amount:
#                 nums[amount] = min(nums[amount], 1 + nums[amount - coin])
#     return nums[n] if nums[n] != float('inf') else -1

# min_coins = [1, 2, 5, 10, 25, 50]
# custom_coins = [5, 25, 2, 50, 1, 10]
# amount = 113

# print("Custom Dynamic Result:", min_nums_of_coins(amount, min_coins))
# print("=" * 42)
# print("Custom Dynamic Result:", min_nums_of_coins(amount, custom_coins))
# print("=" * 42)

# amounts = [10, 100, 1000, 10000, 100000]

# for amount in amounts:
#     print(f"Amount: {amount}")
#     greedy_time = measure_execution_time(find_coins_greedy, amount, greedy_coins)
#     dynamic_time = measure_execution_time(find_min_coins, amount, min_coins)
#     custom_time = measure_execution_time(min_nums_of_coins, amount, min_coins)
#     print(f"Greedy algorithm time: {greedy_time} milliseconds")
#     print(f"Dynamic algorithm time: {dynamic_time} milliseconds")
#     print(f"Custom algorithm time: {custom_time} milliseconds")
#     print("=" * 42)