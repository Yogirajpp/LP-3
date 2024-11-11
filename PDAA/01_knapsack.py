def zero_one_knapsack():
    # Taking dynamic input from the user
    n = int(input("Enter the number of items: "))
    val = list(map(int, input("Enter the values of the items separated by spaces: ").split()))
    wt = list(map(int, input("Enter the weights of the items separated by spaces: ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))

    if len(val) != n or len(wt) != n:
        print("Error: The number of values and weights must match the number of items.")
        return

    # Recursive function for 0/1 Knapsack
    def knapsack(W, n):
        if n < 0 or W <= 0:
            return 0
        if wt[n] > W:
            return knapsack(W, n - 1)
        else:
            return max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))

    print("Maximum value in 0/1 Knapsack:", knapsack(capacity, n - 1))

if __name__ == "__main__":
    zero_one_knapsack()
