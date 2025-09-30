#!/usr/bin/python
"A module that manages student grades"


students = ["alice", "bob", " charlie"]

grades = {}


for student in students:
    print(f"\nenter 3 scores for{student}:")
    scores = []
    for i in range(1, 4):
        score = int(input(f"  score{i}: "))
        scores.append(score)
    grades[student] = scores

print("\naverage scores:")
averages = {}
for student, scores in grades.items():
    avg = sum(scores) / len(scores)
    averages[student] = avg
    print(f"{student}: {avg:.2f}")


top_student = max(averages, key=averages.get)
top_average = averages[top_student]

print(f"\ntop student: {top_student}with an average score of{top_average:.2f}")

