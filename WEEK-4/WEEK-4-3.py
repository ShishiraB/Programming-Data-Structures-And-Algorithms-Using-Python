marks = {"Quizzes":{"Mahesh":[3,5,7,8],"Suresh":[9,4,8,8],"Uma":[9,9,7,6]},"Exams":{"Mahesh":[37],"Uma":[36]}}
#marks["Exams"]["Suresh"].extend([44])
marks["Exams"]["Suresh"] = [44]
#marks["Exams"]["Suresh"].append(44)
#marks["Exams"]["Suresh"][0:] = [44]
print(marks)