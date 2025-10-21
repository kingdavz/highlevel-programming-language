#!/usr/bin/python
"""A module that manages student records"""


def student_record():
    filename = "student.txt"

    with open(filename, "w") as file:
        while True:
            name = input("Enter student name(or 'done' to finish): ")
            if name.lower() == "done":
                break

            score_input = input(f"Enter score for {name}: ")
            try:
                score = float(score_input)
                if score < 0:
                    print("Score cannot be negative. Try again.")
                    continue
            except ValueError:
                print("Invalid score. Try again.")
                continue
            file.write(f"{name}, {score}\n")

    students = []
    with open(filename, "r") as file:
        for line in file:
            name, score = line.strip().split(" ")
            students.append((name, float(score)))

    if not students:
        print("NO student data found.")
        return
    
    highest_score = students[0][1]
    lowest_score = students[0][1]
    total = 0

    for name, score in students:
        if score > highest_score:
            highest_score = score
        if score < lowest_score:
            lowest_score = score
        total += score

    average = total / len(students)

    print("\n=== Students Score report ===")
    print(f"HIghest score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Average Score: {average:.2f}")
    print("============================")
student_record()    
