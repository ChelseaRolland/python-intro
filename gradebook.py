#Last Semester
last_semester_gradebook = [
    ("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

#Current Semester
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append("Computer Science")
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(("Visual Arts", 93))
print(gradebook)

#All together now
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
