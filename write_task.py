import pandas
from task_1 import df_agg as df1
from task_2 import df_agg as df2
from task_3 import df_agg as df3
from openpyxl import load_workbook

xl_file = '.\\data\\Uslugi.xlsx'
book = load_workbook(xl_file)
writer = pandas.ExcelWriter(xl_file, engine='openpyxl')
writer.book = book

df = [df1, df2, df3]

for i in range(3):
    df[i].to_excel(writer, sheet_name='Task_'+str(i+1))

writer.save()
writer.close()