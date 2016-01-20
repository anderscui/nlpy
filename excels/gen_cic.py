from xlrd import open_workbook
from cic_prep import existing_cats, units, course_type_id

wb = open_workbook('cic3.xlsx')

# categories
sheet = wb.sheets()[2]
assert sheet.nrows == 25
assert sheet.ncols == 3

nrows = 25
ncols = 3

all_cats = {}
for row in range(1, nrows):
    cat_id = int(float(sheet.cell(row, 0).value))
    cat_name = sheet.cell(row, 1).value.strip()

    # print cat_id, cat_name
    all_cats[cat_name] = cat_id

assert len(all_cats) == (nrows-1)

# unit items
sheet = wb.sheets()[0]

nrows = sheet.nrows
ncols = sheet.ncols

nrows = 87
ncols = 5

# columns
# 0: Unit, 1: Category, 2: Category BlurbId 3: Item BlurbId, 4: Item English

rows = []
for row in range(1, nrows):
    values = []
    for col in range(ncols):
        value = sheet.cell(row, col).value
        try:
            value = int(float(value))
        except ValueError:
            pass

        values.append(value)

    # print values
    rows.append(values)

cur_unit = ''
item_sql = u"INSERT INTO CourseLevelUnitItem(Name, Description, CourseLevelUnit_id, IsDefaultSelected, InsertDate, InsertBy_id, SaveDate, SaveBy_id, UpdateDate, CourseLevelUnitItemCategory_id, TextResource_id) VALUES ('{0}', '{1}', {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10})"
for row in rows:
    if row[0]:
        cur_unit = 'U' + str(row[0])

    unit_id = units[cur_unit]
    cat_name = row[1].strip()
    cat_id = all_cats[cat_name]

    item_name = row[4].strip().replace("'", "''")
    item_desc = item_name
    item_blurb_id = row[3]
    default_selected = 0

    insert_date = 'GETUTCDATE()'
    insert_by = -1
    save_date = insert_date
    save_by = insert_by
    update_date = insert_date

    if not item_name:
        # print 'empty item'
        continue

    print item_sql.format(item_name, item_desc, unit_id, default_selected, insert_date, insert_by, save_date, save_by, update_date, cat_id, item_blurb_id)
