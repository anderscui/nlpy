# coding=utf-8
import codecs

fname = 'output.txt'
content = '\u4e00\u4e01\u4e03'
cn = content.decode('unicode-escape')
print(cn)
print(len(cn))
print(type(cn))

with codecs.open(fname, 'w', 'utf-8') as f:
    f.write(cn)

# import codecs
# f = codecs.open(fname, 'w', 'utf-8')
# txt = unicode("campeón\n", 'utf-8')
# f.write(txt)
# f.write(content + '\n')
# f.write(content)
# f.close()
