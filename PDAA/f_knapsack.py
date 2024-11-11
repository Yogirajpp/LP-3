def fractional_knapsack():
    # Taking dynamic input from the user
    n = int(input("Enter the number of items: "))
    val = list(map(int, input("Enter the values of the items separated by spaces: ").split()))
    wt = list(map(int, input("Enter the weights of the items separated by spaces: ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))

    if len(val) != n or len(wt) != n:
        print("Error: The number of values and weights must match the number of items.")
        return

    # Pair items by (value-to-weight ratio, weight, value)
    items = sorted(zip(val, wt), key=lambda x: x[0] / x[1], reverse=True)
    max_value = 0

    for value, weight in items:
        if capacity <= 0:
            break
        if weight <= capacity:
            max_value += value
            capacity -= weight
        else:
            max_value += value * (capacity / weight)
            capacity = 0

    print("Maximum value in Fractional Knapsack:", max_value)

if __name__ == "__main__":
    fractional_knapsack()
