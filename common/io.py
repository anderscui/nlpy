
def write_obj(file_name, obj):
    with open(file_name, 'w') as f:
        f.write(str(obj))


def write_str(file_name, s):
    with open(file_name, 'w') as f:
        f.write(s)


def write_line(f, s):
    if isinstance(s, basestring):
        f.write(s)
    else:
        f.write(str(s))
    f.write('\n')


def write_lines(file_name, lines):
    with open(file_name, 'w') as f:
        f.writelines(lines)


def read_all(file_name):
    with open(file_name) as f:
        return f.read()


def read_lines(file_name):
    with open(file_name) as f:
        return f.readlines()


