# Question 3

import string
with open("sample-file.txt", "r") as file:
    lines = file.readlines()

normalized_groups = {}

for index, line in enumerate(lines, start = 1):
    original = line.rstrip()

    normalized = original.lower()
    normalized = normalized.translate(str.maketrans("", "", string.whitespace + string.punctuation))

    if normalized in normalized_groups:
        normalized_groups[normalized].append((index, original))
    else:
        normalized_groups[normalized] = [(index, original)]

duplicate_sets = [group for group in normalized_groups.values() if len(group) > 1]

print("Number of near duplicate sets:", len(duplicate_sets))

for i, group in enumerate(duplicate_sets[:2], start=1):
    print(f"\nSet {i}:")
    for line_num, text in group:
        print(f"{line_num}. {text}")