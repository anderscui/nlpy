from xlrd import open_workbook
from excels.outcomes import Report, Category, Subcategory

wb = open_workbook('outcomes.xlsx')
# print type(wb)
print type(wb.sheets())

sheet = wb.sheets()[0]

nrows = sheet.nrows
ncols = sheet.ncols


# columns
# 0: PR, 1: Category, 2: Subcategory, 3: English
ncols = 4

rows = []
for row in range(1, nrows):
    values = []
    for col in range(ncols):
        value = sheet.cell(row, col).value
        values.append(value)

    rows.append(values)

outcomes = []

cur_report = Report('')
cur_category = Category('')
cur_subcat = Subcategory('')

for r in rows:
    if r[0]:
        # print 'new report'
        cur_report = Report(r[0])
        outcomes.append(cur_report)

    if r[1]:
        # print '\t'*1 + 'new cat'
        cur_category = Category(r[1])
        cur_report.cats.append(cur_category)

    if r[2]:
        # print '\t'*2 + 'new sub'
        cur_subcat = Subcategory(r[2])
        cur_category.subcats.append(cur_subcat)

    if r[3]:
        # print '\t'*3 + 'new blurb'
        cur_subcat.items.append(r[3])

for r in outcomes:
    print r.html()
    for cat in r.cats:
        print cat.name
        print '\t' + cat.html()
        # for subcat in cat.subcats:
        #     print '\t\t' + subcat.html()