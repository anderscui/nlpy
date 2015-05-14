import glob
import os

print(os.getcwdu())

os.chdir('../crawlers/html')
existing = glob.glob1('detail', u'Python_*.html')
print(existing)