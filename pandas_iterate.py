import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for key in student_dict:
#     print(key)
#
# for value in student_dict.items():
#     print(value)
#
# for (key, value) in student_dict.items():
#     print(key, value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

# loop through row if dataframe
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)