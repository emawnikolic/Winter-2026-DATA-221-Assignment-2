# Question 6

import pandas as pd

df = pd.read_csv("crime.csv")

df["risk"] = df["ViolentCrimesPerPop"].apply(lambda x:"HighCrime" if x >= 0.50 else "LowCrime")

avg_unemployment = df.groupby("risk")["PctUnemployed"].mean()

print("Average unemployment rate by crime risk level:")

for risk_level, avg in avg_unemployment.items():
    print(f"{risk_level}: {avg:.2f}%")