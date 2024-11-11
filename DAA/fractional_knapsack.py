def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0

    for weight, value in items:
        if capacity <= 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            capacity = 0

    return total_value

if __name__ == "__main__":
    weights = list(map(int, input("Enter weights (comma-separated): ").split(',')))
    values = list(map(int, input("Enter values (comma-separated): ").split(',')))
    capacity = int(input("Enter knapsack capacity: "))

    if len(weights) != len(values):
        print("Number of weights and values must match.")
    else:
        result = fractional_knapsack(weights, values, capacity)
        print(f"Maximum value in the knapsack: {result}")
