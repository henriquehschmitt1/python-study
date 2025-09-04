pointsPossible = 110
# studentScore = 76
# studentScore = (studentScore / pointsPossible) * 100
# studentScore = round(studentScore, 1)
# name = "John"


# '''
# A - 100-90%
# B - 89-80%
# C - 79-70% 
# D - 69-60%
# F - 59-0%
# '''
# print(studentScore)
#Print the student name and what grade they got

def printGrade(name, score):
    if score >= 90:
        print(f"{name} got an A")
    elif score >= 80:
        print(f"{name} got a B")
    elif score >= 70:
        print(f"{name} got a C")
    elif score >= 60:
        print(f"{name} got a D")
    else:
        print(f"{name} got an F")

students = ["John", "Jane", "Doe", "Mary", "Tom"]
scores = [76, 85, 92, 67, 54]

for i in range(5):
    score = (scores[i] / pointsPossible) * 100
    score = round(score, 1)
    printGrade(students[i], scores[i])
