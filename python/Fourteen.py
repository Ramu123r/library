# 14. Write a python program to search an element using linear equation.
arr = [10, 20, 30, 40, 50]
key = 30

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at position", i + 1)
        break
else:
    print("Element not found")