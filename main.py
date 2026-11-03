scores = [85, 72, 90, 68, 95]

average = sum(scores)/ len(scores)

print("Average Score: ", average)

highest = max(scores)
print("Highest Score: ",highest)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Letter grade: ", grade)