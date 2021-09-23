# # Test file
# import pandas as pd
# xl = pd.ExcelFile('data.xlsx')
# # get the first sheet as an object
# df = pd.read_excel(xl, 0, header=None)
# # print(df)
# # print (len(df))
# # print(df.iloc[1, :])
# # print(df.iloc[8, :][3])
# data = []
# for i in range(len(df)):
#     if not pd.isnull(df.iloc[i, :][3]):
#         # print(df.iloc[i, :])
#         data.append(df.iloc[i, :])
# print(data)
# # if 


import openpyxl

wb = openpyxl.load_workbook('data.xlsx')


# print(wb.sheetnames)

sheet = wb['Sheet1']

# g_all = sheet.values
# print(list(g_all))


data = [[cell.value for cell in row] for row in sheet]

# print(data[1])
# print(len(data))

for No, Topic, Date, Status in data:
    if Status != 'Done':
        print(Topic)
