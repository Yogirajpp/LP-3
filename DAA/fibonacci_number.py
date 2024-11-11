def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def non_recursive_fibonacci(n):
    first, second = 0, 1
    print(first, end=" ")
    for i in range(n - 1):
        print(second, end=" ")
        first, second = second, first + second
    print()

if __name__ == "__main__":
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))

    print("\nFibonacci sequence using recursive approach:")
    for i in range(n):
        print(recursive_fibonacci(i), end=" ")
    
    print("\n\nFibonacci sequence using non-recursive approach:")
    non_recursive_fibonacci(n)



