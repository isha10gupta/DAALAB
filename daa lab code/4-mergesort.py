#merge sorting - sorting an array by dividing it 
#divide and conqure approach 
#TC- O(nlog(n))
#take array user input
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
#function to sort the given array
def merge(arr):
 if len(arr)>1:
    mid=len(arr)//2
    left=merge(arr[:mid]) # Starting index of left subarray
    right=merge(arr[mid:]) # Starting index of right subarray
    i=0
    j=0
    k=0
    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.
    while i<len(left) and j<len(right):
    # There will be no swaping if arr[i] <= arr[j]
      if left[i]>right[j]:
        arr[k]=right[j]
        j+=1
      else:
        arr[k]=left[i]
        i+=1
      k+=1
    # Copy the remaining elements of left
    while i<len(left):
      arr[k]=left[i]
      i+=1
      k+=1
    # Copy the remaining elements of right
    while j<len(right):
      arr[k]=right[j]
      j+=1
      k+=1
 return arr

print(merge(arr))