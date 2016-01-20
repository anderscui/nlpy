class Subcategory(object):
    def __init__(self, name):
        self.name = name
        self.items = []

    def html(self):
        items_html = ''
        if self.items:
            items_html = u', '.join([u"{0}".format(item.replace("'", "''")) for item in self.items])
        return u"<p><strong><em>{0}</em></strong>: {1}</p>".format(self.name, items_html)


class Category(object):
    def __init__(self, name):
        self.name = name
        self.subcats = []

    def html(self):
        return u''.join([sub.html() for sub in self.subcats])


class Report(object):
    def __init__(self, name):
        self.name = name
        self.cats = []

    def html(self):
        return self.name