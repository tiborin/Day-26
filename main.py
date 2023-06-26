
# lost = [1, 2, 3]
# list = [x+1 for x in lost]
# print(list)
#
# name = "Angela"
# new_list = [letter for letter in name]
# print(name)
# print(new_list)
#
# rng = [n*2 for n in range(1, 5)]
# print(rng)

import random
names = ["Angela", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#short_names = [name.upper() for name in names if len(name) < 5]
#print(short_names)

student_score = {student:random.randint(1,100) for student in names}

print(student_score)

passed_students = {student:score for (student, score) in student_score.items() if score > 75}

print(passed_students)