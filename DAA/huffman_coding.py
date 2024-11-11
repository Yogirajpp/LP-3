import heapq

# Define a node for the Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # Frequency of symbol
        self.symbol = symbol  # Character
        self.left = left  # Left child
        self.right = right  # Right child

    def __lt__(self, other):  # Define less than for heap
        return self.freq < other.freq

# Function to print Huffman codes
def print_codes(node, code=''):
    if node is None:
        return
    if not node.left and not node.right:  # Leaf node
        print(f"{node.symbol} -> {code}")
    print_codes(node.left, code + '0')
    print_codes(node.right, code + '1')

# Main Huffman coding function
def huffman_coding(chars, freqs):
    heap = [Node(freqs[i], chars[i]) for i in range(len(chars))]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(heap, merged)

    print("Huffman Codes:")
    print_codes(heap[0])

if __name__ == "__main__":
    chars = input("Enter characters (comma-separated): ").split(',')
    freqs = list(map(int, input("Enter frequencies (comma-separated): ").split(',')))

    if len(chars) != len(freqs):
        print("Number of characters and frequencies must match.")
    else:
        huffman_coding(chars, freqs)
