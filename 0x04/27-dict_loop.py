#!/usr/in/pyton
"A module tah loops throug a dictionary"

scores = {"alice": 85, "bob": 90, "charlie": 78, "diana": 92}
print("stuents who scored above 80: ")
for student, score in scores.items():
    if score > 80:
        print(f"{student}: {score}")

highest_scorer = max(scores, key=scores.get)
highest_score = scores[highest_scorer]

print(f"\nhighest score: ")
print(f"{highest_scorer}: {highest_score}")