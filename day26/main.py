# # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # # 🚨 Do Not Change the code above 👆
# #
# # #Write your 1 line code 👇 below:
# # squared_numbers = [pow(num, 2) for num in numbers]
# #
# # #Write your code 👆 above:
# #
# # print(squared_numbers)
# #
# #
# # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # # 🚨 Do Not Change the code above
# #
# # # Write your 1 line code 👇 below:
# # result = [num for num in numbers if num % 2 == 0]
# #
# # # Write your code 👆 above:
# #
# # print(result)
# with open("file1.txt", mode="r") as f:
#     nums1 = f.readlines()
#     nums1 = [int(i.replace("\n", "")) for i in nums1]
#
# with open("file2.txt", mode="r") as f:
#     nums2 = f.readlines()
#     nums2 = [int(i.replace("\n", "")) for i in nums2]
#
# result = [num for num in nums1 if num in nums2]
#
# # Write your code above 👆
#
# print(nums1)
# print(nums2)
# print(result)
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Steve']
#
# import random
#
# students_score = {student: random.randint(1, 100) for student in names}
#
# passed_students = {student: score for (student, score) in students_score.items() if score > 50}
# print(passed_students)

#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {word: len(word) for word in sentence.split()}
#
#
# print(result)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
#
#
# print(weather_f)

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

words = []
for elem in df.values:
    elements = [value for value in elem]
    words.append(elements)

alphabet = {key[0]: key[1] for key in words}

while True:
    word = input("Input the word: ")
    say = {letter: alphabet[letter.upper()] for letter in word}
    print(say)
