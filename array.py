import sys

if len(sys.argv) < 2:
    print("Please provide an array of scores.")
    sys.exit(1)

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)

print("Array of Scores:", scores)
print("Sum of Scores:", total)
print("Average of Scores:", average)