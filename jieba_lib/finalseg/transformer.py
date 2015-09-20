import json


def json_dump(obj, f):
    json.dump(obj, f, indent=2, separators=(',', ': '))


# # prob_trans
# import prob_trans
# p_trans = prob_trans.P
#
# with open('prob_trans.json', 'w') as f:
#     json_dump(p_trans, f)


# prob_emit
import prob_emit

p_emit = prob_emit.P
with open('prob_emit.json', 'w') as f:
    json_dump(p_emit, f)
