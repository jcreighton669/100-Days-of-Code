numbers = [1, 2, 3]

new_numbers = [number + 1 for number in numbers]

# print(new_numbers)

name = "Justin"

letter_name = [letter for letter in name]
# print(letter_name)

doubled_numbers = [num * 2 for num in range(1, 5)]
print(doubled_numbers)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
