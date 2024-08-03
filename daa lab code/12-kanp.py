#TC-O(n*W)
#Dynamic programming approach 

# Taking input from the user for the number of items
n = int(input("Enter the number of items: "))
profit = []
weight = []
# Taking input for the profit and weight of each item
for i in range(n):
    p = int(input(f"Enter profit for item {i+1}: "))
    w = int(input(f"Enter weight for item {i+1}: "))
    profit.append(p)
    weight.append(w)
# Taking input for the capacity of the knapsack
W = int(input("Enter the capacity of the knapsack: "))

#func to determine th array
def knapSack(W, wt, val, n):
    # Initialize a table to store the maximum value for each subproblem
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build the table K[][] in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                # Base case: if there are no items or weight capacity is 0,
                # the maximum value is 0
                K[i][w] = 0
            elif wt[i-1] <= w:
                # If the weight of the current item is less than or equal to
                # the current capacity, consider including the item
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                # If the weight of the current item is more than the current
                # capacity, do not include the item
                K[i][w] = K[i-1][w]
    # Return the maximum value that can be put in a knapsack of capacity W
    return K[n][W]

# Print the maximum value that can be put in the knapsack
print("The maximum value that can be put in the knapsack is:", knapSack(W, weight, profit, n))
