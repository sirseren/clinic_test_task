import pandas

pandas.set_option('display.max_columns', None)
#import file
xl_file = '.\\data\\Uslugi.xlsx'

xl_data = pandas.ExcelFile(xl_file)
df_data = xl_data.parse(xl_data.sheet_names[0])

aggregations = {
    'Стоимость': sum
}

df_agg = df_data.groupby(['Филиал','Специализация']).agg(aggregations)\
    .reset_index()\
    .rename(columns={('Услуга'): 'Кол-во услуг', 'Стоимость':'Выручка (сколько заработал врач)'})


if __name__ == "__main__":
    print(df_agg)