import json

# f = -4.76230521459696789
# print '%.15f' % f


def key_of_pos_state(ps):
    return ps[0] + '-' + ps[1]


def json_dump(obj, f):
    json.dump(obj, f, indent=2, separators=(',', ': '))


# # prob_start
# import prob_start
#
# p_start = prob_start.P
# result_start = {}
# for k in p_start:
#     result_start[key_of_pos_state(k)] = p_start[k]
#
# print len(p_start)
#
# with open('pos_prob_start.json', 'w') as f:
#     json_dump(result_start, f)
#
#
# # prob_trans
# import prob_trans
# p_trans = prob_trans.P
# keys = p_trans.keys()
#
# result_trans = {}
# total = 0
# for k_from in keys:
#     states_to = {}
#     for k in p_trans[k_from]:
#         states_to[key_of_pos_state(k)] = p_trans[k_from][k]
#     result_trans[key_of_pos_state(k_from)] = states_to
#     total += len(p_trans[k_from])
#
# print(len(keys))
# print total
#
# with open('pos_prob_trans.json', 'w') as f:
#     json_dump(result_trans, f)


# # prob_emit
# import prob_emit
#
# p_emit = prob_emit.P
# assert len(p_emit) == 256
#
# keys = sorted(p_emit.keys())
#
# result_emit = {}
# total = 0
# for k in keys:
#     result_emit[key_of_pos_state(k)] = p_emit[k]
#     total += len(p_emit[k])
#
# print total
#
# with open('pos_prob_emit.json', 'w') as f:
#     json_dump(result_emit, f)


# prob_state_tab
import char_state_tab
state_tab = char_state_tab.P

result_state_tab = {}
total = 0
for k in state_tab:
    total += len(state_tab[k])
    result_state_tab[k] = [key_of_pos_state(p) for p in state_tab[k]]

print len(state_tab)
print total

with open('char_state_tab.json', 'w') as f:
    json_dump(result_state_tab, f)