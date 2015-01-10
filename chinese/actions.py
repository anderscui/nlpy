import csv
import jieba


class Action():
    def __init__(self, aid, cid, note):
        self.aid = aid
        self.cid = cid
        self.note = note


def read_data():
    fname = './customers.txt'
    actions = []

    with open(fname, 'r') as f:
        next(f)  # skip headers
        reader = csv.reader(f, delimiter='\t')
        for aid, cid, note in reader:
            actions.append(Action(aid, cid, note))

    return actions

if __name__ == '__main__':
    actions = read_data()
    tokens = []
    # for i in range(-20, -1):
    #     seg_list = jieba.cut(actions[i].note, cut_all=False)
    #     print "/ ".join(seg_list)
    for act in actions:
        seg_list = jieba.cut(act.note, cut_all=False)
        tokens.append((act.cid, list(seg_list)))

    print(len(tokens))

