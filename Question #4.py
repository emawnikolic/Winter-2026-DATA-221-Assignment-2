# Question 4

import pandas as pd

df = pd.read_csv("student.csv")
filtered_df = df [(df["study_time"] >= 3) & (df["internet"] == 1) & (df["absences"] <= 5)]

filtered_df.to_csv("high_engagement.csv", index=False)

num_students = len(filtered_df)
average_grade = filtered_df["grade"].mean()

print("Number of students saved:", num_students)
print("average grade:", average_grade)