import pandas as pd

data = {'이름' : ['Kim', 'Park', 'Lee', 'Ho'],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88] }
df = pd.DataFrame(data)

print("1> --------------------------------------")
print("국어 평균 : ", df['국어'].mean(), end="\n\n")
print("국어 중간 : ", df['국어'].median(), end="\n\n")
print("국어 최소 : ", df['국어'].min(), end="\n\n")
print("국어 최대 : ", df['국어'].max(), end="\n\n")

print("2> --------------------------------------")
print("Kim 총점 : ", df.iloc[0, 1:4].sum(), end="\n\n")
print("Kom 평균 : ", df.iloc[0, 1:4].mean(), end="\n\n")

print("3> --------------------------------------")
print("수학 4분위 \n", df['수학'].quantile([0.25,0.5,0.75]), end="\n\n")
print("수학 분산 : ", df['수학'].var(), end="\n\n")
print("수학 표준편차 : ", df['수학'].std(), end="\n\n")