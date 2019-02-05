import pandas

#import file
xl_file = '.\\data\\Uslugi.xlsx'

xl_data = pandas.ExcelFile(xl_file)
df_data = xl_data.parse(xl_data.sheet_names[0])

aggregations = {
    'Услуга': "count",
    'Стоимость': sum
}

df_agg = df_data.groupby(['Филиал']).agg(aggregations)\
    .reset_index()\
    .rename(columns={('Услуга'): 'Кол-во услуг', 'Стоимость':'Сумма на которую оказали услуги'}) #just rename


if __name__ == "__main__":
    print(df_agg)