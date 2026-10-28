def replace_value(values, index, new_value):
    values[index] = new_value
    return None

def find_first(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1

def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record

original = []

number_of_days = int(input("Enter the number of days: "))
for cooking in range(number_of_days):
    cooking_time = int(input("Enter cooking time in minutes: "))
    original.append(cooking_time)

updated = original[:]

index = int(input("Enter the index to correct: "))
new_cooking_time = int(input("Enter the new cooking time: "))

replace_value(updated, index, new_cooking_time)

search_cooking_time = int(input("Enter the cooking time to search for: "))
time_targets = find_first(updated, search_cooking_time)
counted_target = updated.count(search_cooking_time)
minimum, maximum, total = summarize(updated)
sorted_updated = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_updated}")
print(f"Minimum cooking time: {minimum} minutes")
print(f"Maximum cooking time: {maximum} minutes")
print(f"Total cooking time: {total} minutes")

if time_targets == -1:
    print("Target not found")
else:
    print(f"First matching index: {time_targets}")

print(f"Matching values: {counted_target}")
