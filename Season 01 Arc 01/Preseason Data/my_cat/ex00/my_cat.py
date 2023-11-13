import sys

ruyxat = sys.argv
# print(ruyxat)

for n in ruyxat[1:]:
    fayil1 = open(n, 'r')
    print(fayil1.read().strip())
