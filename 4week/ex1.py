import pandas as pd

data = {'이름' : ['Kim', 'Park', 'Lee', 'Ho'],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88] }

print("1> --------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")

print("2> --------------------------------------")
sr_name = df['이름']
print(sr_name, end="\n\n")

print("3> --------------------------------------")
park_data = df.loc[1]
park_data = df.loc[df['이름'] == 'Park']
print(park_data, end="\n\n")

print("4> --------------------------------------")
df.loc[df['이름'] == 'Ho', '수학'] = 90
print(df, end="\n\n")

print("5> --------------------------------------")
df.loc[3] = ['Oh', 100, 70, 80]
print(df, end="\n\n")

print("6> --------------------------------------")
df = df.drop([2], axis=0)
print(df, end="\n\n")