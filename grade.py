def calculation_grade_final_my(filename):
    with open(filename) as f:
        lines = f.readlines()
    grades = {}
    for line in lines:
        data = line.strip().split(',')
        name = data[0]
        quizzes = [int(x) for x in data[1:7]]
        assignments = [int(x) for x in data[7:11]]
        midterm = int(data[11])
        final = int(data[12])
        quiz_avg = sum(sorted(quizzes)[-5:]) / 5
        assign_avg = sum(sorted(assignments)[-3:]) / 3
        final_grade = quiz_avg * 0.3 + assign_avg * 0.4 + midterm * 0.1 + final * 0.2
        if final_grade >= 60:
            grades[name] = 'Pass'
        else:
            grades[name] = 'Fail'
    return grades
file_name = "E:\myproje\score.txt"
x = calculation_grade_final_my(file_name)
print(x)