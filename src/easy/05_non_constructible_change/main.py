def non_constructible_change(coins: list[int]) -> int:
    if len(coins) == 0:
        return 1
    coins.sort()
    coin_sum = 0
    for index, coin in enumerate(coins):
        if index == 0 and coin >= 2:
            return 1
        if index == 0:
            coin_sum += coin
            continue
        if coin <= coin_sum + 1:
            coin_sum += coin
            continue
        return coin_sum + 1
    return coin_sum + 1


if __name__ == "__main__":
    non_constructible_change([5, 7, 1, 1, 2, 3, 22])
