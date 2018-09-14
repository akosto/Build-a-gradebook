last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry", "history"]
subjects.append("computer science")
grades = [98, 97, 85, 88]
grades.append(100)
gradebook = list(zip(subjects, grades))
subjects.append("visual arts")
grades.append(93)
print(gradebook)
last_subjects = ["chemistry", "algebra", "philosophy", "law"]
last_grades = [86, 92, 76, 80]
last_semester_gradebook = list(zip(last_subjects, last_grades))
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)

