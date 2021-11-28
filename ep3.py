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

logins = logins.rename(columns={'login': 'User'})

data = results.merge(logins)
mean_f_data = data.groupby('group_faculty').mean()

fig, axs = plt.subplots(2, 1)
axs[0].set_title("Solved per faculty group")
axs[0].bar(mean_f_data.index[:], mean_f_data['Solved'], color='blue')

mean_out_data = data.groupby('group_out').mean()

axs[1].set_title("Solved per informatics group")
axs[1].bar(mean_out_data.index[:], mean_out_data['Solved'], color='red')

clever_students = data[(data['G'] > 10) | (data['H'] > 10)]
clever_facult_groups = clever_students.groupby('group_faculty').count().index[:]
clever_inf_groups = clever_students.groupby('group_out').count().index[:]

print("Группы, студенты которых прошли более 1 теста в G и H:")
print(*clever_facult_groups, sep=', ')
print("Группы по информатике, студенты которых прошли более 1 теста в G и H:")
print(*clever_inf_groups, sep=', ')

plt.show()
