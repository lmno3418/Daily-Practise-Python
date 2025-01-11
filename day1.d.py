# Convert seconds to hours, minutes, and seconds.#
s = 64543453

"""h=int(s/3600)
m=int(s/60)
print(h,m,s)
"""

# Use // for integer division

h = s // 3600
s = s % 3600
m = s // 60
s = s % 60

print(h, m, s)
