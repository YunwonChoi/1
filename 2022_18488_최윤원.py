import pandas as pd
import numpy as np
data = {"Name": pd.Series(["Avery Bradley", "Jae Crowder", "John Holland", "R.J. Hunter", "Jonas Jerebko"]),
        "Position": pd.Series(["SG", "SF", "SG", "SG", "PF"]),
        "Age": pd.Series([25, 25, 27, 22, 29]),
        "Height": pd.Series([170, 175, 180, 172, 171]),
        "Weight": pd.Series([85, 80, 90, 90, 85])}
df = pd.DataFrame(data)
val = pd.Series(["Texas", "Marguetta", "Texas", "Georgia State"], index = [0, 1, 2, 3])
df['College'] = val
val = pd.Series([7730337, 6796117, 1148640, 5000000], index=[0, 1, 3, 4])
df['Salary'] = val
print('처음')
print(df)
#기능 1 구현
df.loc[:, "Salary"] = df["Salary"].fillna(0)
print('기능 1')
print(df)
#기능 2 구현
df.loc[df['Position'] == "SG", 'Salary'] += 100000
print('기능 2')
print(df)
#기능 3 구현
df.loc[(df['College'] == 'Texas') & (df['Age'] >= 26), 'Salary'] += 100000
print('기능 3')
print(df)
#기능 4 구현
func = lambda x, y: x/(y*0.01)**2
bmi = func(df["Weight"], df["Height"])
df["bmi"] = bmi
df.loc[(df['bmi'] < 24), "BMI"] = "A"
df.loc[(df['bmi'] >= 24) & (df['bmi'] < 28), "BMI"] = "B"
df.loc[(df['bmi'] >= 28), "BMI"] = "C"
del df["bmi"]
print('기능 4')
print(df)
#기능 5 구현
BMI_C = []
for i in range(len(df)):
        if df.iloc[i]["BMI"] == "C":
                BMI_C.append(i)
print('기능 5')
print(df.loc[BMI_C])

