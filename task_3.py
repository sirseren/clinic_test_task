import pandas

pandas.set_option('display.max_columns', None)

#import file
xl_file = '.\\data\\Uslugi.xlsx'

xl_data = pandas.ExcelFile(xl_file)
df_data = xl_data.parse(xl_data.sheet_names[0])\

aggregations = {
    'Стоимость': sum
}

s_agg = df_data.groupby(['Филиал']).Услуга.nunique()
df_agg = pandas.DataFrame(s_agg)\
     .rename(columns={('Услуга'): 'Количество уникальных услуг'})

if __name__ == "__main__":
    print(df_agg)


