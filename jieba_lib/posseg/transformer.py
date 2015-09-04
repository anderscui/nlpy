import json

# f = -4.76230521459696789
# print '%.15f' % f

# import prob_start
# p_start = prob_start.P
# keys = sorted(p_start.keys())
# # i = 0
# # for k in keys:
# #     i += 1
# #     print '%s\t%.16g' % (k, p_start[k])
# #
# # print i
#
# vals = [{'PosState': k[0] + '-' + k[1], 'Prob': p_start[k]} for k in keys]
#
# with open('pos_prob_start.json', 'w') as f:
#     json.dump(vals, f)

def key_of_pos_state(ps):
    return ps[0] + '-' + ps[1]

import prob_trans
p_trans = prob_trans.P
keys = sorted(p_trans.keys())

result_trans = []
for k_from in keys:
    p_trans_to = []
    states_to = p_trans[k_from]
    if states_to:
        keys_to = sorted(states_to.keys())
        p_trans_to = [{'PosState': k_to[0] + '-' + k_to[1], 'Prob': states_to[k_to]} for k_to in keys_to]
    result_trans.append({'PosStateFrom': key_of_pos_state(k_from), 'PosStatesTo': p_trans_to})

with open('pos_prob_trans.json', 'w') as f:
    json.dump(result_trans, f)
