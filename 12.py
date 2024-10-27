# Function to find the index of X in the list of numbers
def find_index(numbers, x):
    try:
        # Find the index of x and return it as 1-based index
        return numbers.index(x) + 1
    except ValueError:
        # Return -1 if x is not found
        return -1

# Main program
def main():
    # Read positive integer N
    N = int(input("Enter a positive integer N: "))
    
    # Ensure N is positive
    if N <= 0:
        print("N must be a positive integer.")
        return

    # Read N numbers one by one
    numbers = []
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Read integer X
    X = int(input("Enter an integer X to search for: "))

    # Find the index of X and print the result
    index = find_index(numbers, X)
    print(index)

# Run the program
if __name__ == "__main__":
    main()
