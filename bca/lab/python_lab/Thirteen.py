# 13. Write a python program to input an array of n numbers and find separately the sum of positive numbers and negative numbers.
arr = [10, -5, 20, -8, 15, -2]

pos_sum = 0
neg_sum = 0

for num in arr:
    if num > 0:
        pos_sum += num
    elif num < 0:
        neg_sum += num

print("Sum of Positive Numbers =", pos_sum)
print("Sum of Negative Numbers =", neg_sum)