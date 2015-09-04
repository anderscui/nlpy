from math import exp
from finalseg.prob_start import P as start_p
from finalseg.prob_trans import P as trans_p

for s in start_p:
    print s, exp(start_p[s])

print

for s in trans_p:
    print 'from ' + s + ' to:'
    for next in trans_p[s]:
        print '\t -> ' + next, exp(trans_p[s][next])

# '\u4e00': -3.6544978750449433
print u'\u4e00\0'
print exp(-3.6544978750449433)

# '\u4e01': -8.125041941842026,
print u'\u4e01\0'
print exp(-8.125041941842026)

# '\u6559': -6.218383963317394,
print u'\u6559\0'
print exp(-6.218383963317394)


#'B': '\u4e00': -3.6544978750449433
#'E': '\u4e00': -6.044987536255073,
#'M': '\u4e00': -4.428158526435913,
#'S': '\u4e00': -4.92368982120877,