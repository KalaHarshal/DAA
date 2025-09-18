def knapsack(max_weight, weights, values, item_count):
    table = [[0 for x in range(max_weight + 1)] for y in range(item_count + 1)]

    for i in range(item_count + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif weights[i - 1] <= w:
                take = values[i - 1] + table[i - 1][w - weights[i - 1]]
                skip = table[i - 1][w]
                table[i][w] = max(take, skip)
            else:
                table[i][w] = table[i - 1][w]

    return table[item_count][max_weight]

# Example use
values = [60, 100, 120]
weights = [10, 20, 30]
max_bag_weight = 50
items = len(values)

print(knapsack(max_bag_weight, weights, values, items))
