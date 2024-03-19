def gradechange(grade):
    
    gradelist = {"A+": 4.5,"A0": 4.0,"B+": 3.5,"B0": 3.0,
                 "C+": 2.5,"C0": 2.0,"D+": 1.5,"D0": 1.0,
                 "F" : 0.0 }
    
    if grade in gradelist:

        result = gradelist[grade]
        return result
    

total_credit = 0.0
total_grade_point = 0.0

for i in range(20):
    info = list(map(str, input().split()))
    if info[2] == "P":
        continue
    else:
        total_credit += float(info[1])
        total_grade_point += float(info[1]) * gradechange(info[2])

total_GPA = total_grade_point / total_credit
print(total_GPA)
