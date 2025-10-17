
#sample input scores
story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

scoring_criteria = [story, text, role, director, cast]

score_chart = {
# grade [story, text, role, director, cast]
    "A": [6, 5, 4, 3, 2],
    "B": [5, 4, 3, 2, 1],
    "C": [4, 3, 2, 1, 0],
    "D": [2, 1, 1, 0, 0],
    "F": [0, 0, 0, 0, 0]
}

total_score = 0
                  
for index, grade in enumerate(scoring_criteria):
    score = score_chart[grade][index]
    total_score += score

message = ""
if total_score >= 20:
    total_score = 20
    message = "Perfect score"
elif total_score >= 17:
    message = "Must do"
elif total_score >= 14:
    message = "Seriously consider"
elif total_score >= 12:
    message = "On the bubble"
else:
    message = "Pass"

print(total_score)
print(message)