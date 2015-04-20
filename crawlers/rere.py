import re

pat = re.compile(r'hello')
m1 = pat.match('hello world!')
m2 = pat.match('helloo world!')
m3 = pat.match('helllo world!')
m4 = pat.match('hello hello world!')

if m1:
    print(m1.group())
else:
    print('m1 not match')

if m2:
    print(m2.group())
else:
    print('m2 not match')

if m3:
    print(m3.group())
else:
    print('m3 not match')

if m4:
    # return group(0) only by default
    print(m4.group())

    for g in m4.groups():
        print(g)
else:
    print('m4 not match')

## escape chars
print(re.escape('\d\w\t'))


## search vs. match
print(re.match('super', 'superstition').span())
print(re.match('super', 'insuperable'))

print(re.search('super', 'superstition').span())
print(re.search('super', 'insuperable').span())

## split by regex
pat = re.compile(r'\d+')
print(pat.split('one1two2three3four4'))

## find all instances
pat = re.compile(r'\d+')
print(pat.findall('one1two2three3four4'))

## find iterator
for m in pat.finditer('one1two2three3four4'):
    print(m.group())

## substitute
# use sub method
# subn





