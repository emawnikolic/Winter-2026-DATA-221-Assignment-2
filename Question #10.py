# Question 10

def find_lines_containing(filename, keyword):
    matches = []
    keyword_lower = keyword.lower()

    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if keyword_lower in line.lower():
                matches.append((i, line.rstrip("\n")))
    return matches

filename = "sample-file.txt"
keyword = "lorem"

matching_lines = find_lines_containing(filename, keyword)

print(f"Number of matching lines: {len(matching_lines)}\n")

print("First 3 matching lines:")
for line_number, line_text in matching_lines[:3]:
    print(f"{line_number}: {line_text}")
