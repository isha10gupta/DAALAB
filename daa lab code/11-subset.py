
#TC-O(n*sum)
#Dynamic programming approach 
# Taking input from the user
n = int(input("Enter number of elements: "))
set = [int(input()) for i in range(n)]
sum = int(input("Enter the sum: "))

#function to find the subset of the sum
def subset(set, sum):
    n = len(set)
    # Create a 2D list initialized with 0's. Dimensions are (n+1) x (sum+1) for dp
    arr = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]
    # Fill the DP table
    for i in range(n + 1):
        for j in range(sum + 1):
            # Base case: A sum of 0 can always be achieved with an empty subset
            if j == 0:
                arr[i][j] = 1
            # If the element is greater than the current sum or the subset without this element forms the sum
            elif i == 0 or set[i - 1] > j:
                arr[i][j] = arr[i - 1][j]
            # Otherwise, check if we can form the sum by including this element
            else:
                arr[i][j] = arr[i - 1][j - set[i - 1]] 
    return arr

def find_subset(set, sum, arr):
    n = len(set)
    subset = []
    # Start from the last element and work backwards
    i, j = n, sum
    while i > 0 and j > 0:
        # If the current sum is different from the sum without the current element
        if arr[i][j] != arr[i - 1][j]:
            # The element set[i-1] is part of the subset
            subset.append(set[i - 1])
            # Reduce the sum by this element
            j -= set[i - 1]
        i -= 1 
    return subset

# Call the subset function
arr = subset(set, sum)
# Check if the sum can be formed by any subset
if arr[n][sum]:
    print("Subset exists!")
    # Find and print the subset
    subset_result = find_subset(set, sum, arr)
    print("Subset that sums to", sum, ":", subset_result)
else:
    print("Subset doesn't exist!")
