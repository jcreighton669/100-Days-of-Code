with open("file1.txt") as file_1:
    first_file_data = file_1.read().split()

with open("file2.txt") as file_2:
    second_file_data = file_2.read().split()

result = [num for num in first_file_data if num in second_file_data]

# Write your code above 👆

print(result)
