def solve_knapsack():
    def knapsack(W, weight, val, n):
        # Base case
        if n == 0 or W == 0:
            return 0

        # If weight of the current item exceeds the capacity, skip it
        if weight[n - 1] > W:
            return knapsack(W, weight, val, n - 1)
        else:
            # Maximize value by including or excluding the current item
            return max(
                val[n - 1] + knapsack(W - weight[n - 1], weight, val, n - 1),
                knapsack(W, weight, val, n - 1)
            )

    # Dynamic inputs
    val = list(map(int, input("Enter values (comma-separated): ").split(',')))
    weight = list(map(int, input("Enter weights (comma-separated): ").split(',')))
    W = int(input("Enter knapsack capacity: "))

    if len(val) != len(weight):
        print("Number of values and weights must match.")
    else:
        n = len(val)
        result = knapsack(W, weight, val, n)
        print(f"Maximum value in the knapsack: {result}")

if __name__ == "__main__":
    solve_knapsack()
