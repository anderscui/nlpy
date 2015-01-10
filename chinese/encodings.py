# coding=utf-8

fname = 'output.txt'
content = u'中文'

# f = file(fname, 'w')
# f.write(content)
# f.close()

import codecs
f = codecs.open(fname, 'w', 'utf-8')
txt = unicode("campeón\n", 'utf-8')
f.write(txt)
f.write(content + '\n')
f.write(content)
f.close()