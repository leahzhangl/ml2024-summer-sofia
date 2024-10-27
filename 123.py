def main():
    # Ask for a positive integer N
    N = int(input("Enter a positive integer N: "))
    
    # Initialize a list to store the N numbers
    numbers = []
    
    # Read N numbers one by one
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    # Ask for the integer X to search for
    X = int(input("Enter the integer X to search for: "))
    
    # Check if X is in the list and find its index
    if X in numbers:
        index = numbers.index(X) + 1  # Convert to 1-based index
        print(f"The index of {X} is: {index}")
    else:
        print("-1")  # X not found

if __name__ == "__main__":
    main()
