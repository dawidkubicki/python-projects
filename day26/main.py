# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# squared_numbers = [pow(num, 2) for num in numbers]
#
# #Write your code 👆 above:
#
# print(squared_numbers)
#
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# # Write your 1 line code 👇 below:
# result = [num for num in numbers if num % 2 == 0]
#
# # Write your code 👆 above:
#
# print(result)
with open("file1.txt", mode="r") as f:
    nums1 = f.readlines()
    nums1 = [int(i.replace("\n", "")) for i in nums1]

with open("file2.txt", mode="r") as f:
    nums2 = f.readlines()
    nums2 = [int(i.replace("\n", "")) for i in nums2]

result = [num for num in nums1 if num in nums2]

# Write your code above 👆

print(nums1)
print(nums2)
print(result)
