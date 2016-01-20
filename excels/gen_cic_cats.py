from xlrd import open_workbook
from cic_prep import existing_cats, units, course_type_id

wb = open_workbook('cic3.xlsx')

# categories
sheet = wb.sheets()[1]
assert sheet.nrows == 23
assert sheet.ncols == 2

nrows = 23
ncols = 2

all_cats = {}
for row in range(1, nrows):
    cat_name = sheet.cell(row, 0).value.strip()
    cat_blurb_id = int(float(sheet.cell(row, 1).value))

    # print values
    all_cats[cat_name] = cat_blurb_id

assert len(all_cats) == (nrows-1)

new_cats = [(c, all_cats[c]) for c in all_cats if c not in existing_cats]
new_cats.sort()
# for c in new_cats:
#     print c

tbcoursetypeid_var = '@tbCourseTypeId'
start_cat_id = 25
cat_sql = "INSERT INTO dbo.CourseLevelUnitItemCategory (CourseLevelUnitItemCategory_id, Name, TextResource_id, CourseTypeCode_id) VALUES ({0}, '{1}', {2}, {3})"
for i, c in enumerate(new_cats):
    cat_id = start_cat_id + i
    sql = cat_sql.format(cat_id, c[0], c[1], tbcoursetypeid_var)
    print sql
