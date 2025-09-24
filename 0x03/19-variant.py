#!/usr/bin/python
"""A module that proccess numeric scores and classify them"""


def classify_scores(scores):
    classified = []

    for score in scores:
        if score < 50:
            classified.append(("failure class", score))
        elif score >= 90:
            classified.append(("acheiver class", score))

    return classified


scores = [45, 23, 50, 38, 90, 98, 72, 93, 95,]
result = classify_scores(scores)
print(result)

