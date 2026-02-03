# Question 5

import pandas as pd

df = pd.read_csv("student.csv")

def grade_band(grade):
    if grade <= 9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(grade_band)

df["internet_binary"] = (
    df["internet"]
    .map({"Yes": 1, "No": 0, "yes": 1, "no": 0})
    .fillna(df["internet"])
)

summary = (
    df.groupby("grade_band")
      .agg(
          number_of_students=("grade", "count"),
          average_absences=("absences", "mean"),
          internet_percentage=("internet_binary", "mean")
      )
      .reset_index()
)

summary["internet_percentage"] = summary["internet_percentage"] * 100
summary.to_csv("student_bands.csv", index=False)

print(summary)
