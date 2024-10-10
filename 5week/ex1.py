import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i], ha = 'center')
        
hat = pd.read_csv('ch4-1.csv') 
print(hat.head(), end="\n\n")

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.figure(figsize=(15, 10))
plt.bar(hat['hatchery'], hat['chick'], color = ('red','orange','yellow','green','blue','navy','purple'))
plt.title('hatchery statistics')
plt.xlabel('hatchery')
plt.ylabel('chick count')

addtext(hat['hatchery'], hat['chick'])

plt.show()

print("######### 파이차트를 그리기 위해 비율 계산")

import seaborn as sns
pct = hat['chick']/hat['chick'].sum()
col7 = sns.color_palette('Pastel2', 7)

plt.figure(figsize=(10, 10))
plt.pie(pct, labels = hat['hatchery'], autopct='%.1f%%', colors=col7, counterclock = False)
plt.show()

print("######### 라인 차트 그리기 ")
plt.figsize(figsize=(10, 7))
plt.plot(hat.hatchery, hat.chick, marker='*', color='y', linestyle='--', linewidth=4)
plt.title('부회장별 병아리 부화현황')
plt.xlabel('부회장')
plt.ylabel('부화마릿수')
plt.grid(True)
plt.legend(['부화마릿수'], fontsize=10, loc='best')
plt.show()