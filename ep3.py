import pandas as pd
import re
import numpy as np
from inting import inting
import matplotlib.pyplot as plt
from inting import inting
from collections import defaultdict

with pd.ExcelFile('students_info.xlsx') as xls:
    logins = pd.read_excel(xls, 'logins')

with open('results_ejudge.html', 'r') as html:
    html_text = html.read()
    tbl = re.sub('<a.*?href="(.*?)">(.*?)</a>', '\\1 \\2', html_text)
    results = pd.read_html(tbl)[0]


facult_groups = defaultdict(list)
inf_groups = defaultdict(list)
clever_facult_groups = set()
clever_inf_groups = set()
for index, i in results.iterrows():
    user = i['User']
    solved = i['Solved']
    G = i['G']
    H = i['H']

    if not logins[logins['login'] == user].empty:
        facult_group = logins[logins['login'] == user]['group_faculty'].tolist()[0]
        inf_group = logins[logins['login'] == user]['group_out'].tolist()[0]

        facult_groups[facult_group].append(solved)
        inf_groups[inf_group].append(solved)

        if (pd.notna(G) and G > 10) or (pd.notna(H) and H > 10):
            clever_facult_groups.add(facult_group)
            clever_inf_groups.add(inf_group)


facult_groups_bars = []
facult_groups_data = []
inf_groups_bars = []
inf_groups_data = []
for i in facult_groups.items():
    facult_groups_bars.append(i[0])
    facult_groups_data.append(sum(i[1]) / len(i[1]))

for i in inf_groups.items():
    inf_groups_bars.append(i[0])
    inf_groups_data.append(sum(i[1]) / len(i[1]))

print("Группы, студенты которых прошли более 1 теста в G и H:")
print(*clever_facult_groups, sep='\n')
print("Группы по информатике, студенты которых прошли более 1 теста в G и H:")
print(*clever_inf_groups, sep='\n')

fig, axs = plt.subplots(2, 1)
axs[0].set_title("Solved per faculty group")
axs[0].bar(facult_groups_bars, facult_groups_data, color='blue')

axs[1].set_title("Solved per informatics group")
axs[1].bar(inf_groups_bars, inf_groups_data, color='red')
plt.show()
