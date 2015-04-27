from common.io import read_lines, modified_on, accessed_on, created_on

# file_name = './read_file.txt'
# whole = read(file_name)
# print(type(whole))
# print(whole)
#
# lines = read_lines(file_name)
# print(type(lines))
# print(lines)


# file_name_cn = './read_file_cn.txt'
# whole = read(file_name_cn)
# # print(type(whole))
# print(whole)
#
# lines = read_lines(file_name_cn)
# # print(type(lines))
# print(lines)


filename = r'C:\andersc\works\git\odinplus\Source\ParentPages\EFSchools.EnglishFirst.Parents.sln'
print(created_on(filename))
print(accessed_on(filename))
print(modified_on(filename))

