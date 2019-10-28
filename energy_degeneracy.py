"""
Note: degeneracy values towards the upper bound of the range may be in accurate as an integer combination yielding the
same energy over the upper limit may exist, but the range specified may not take it into account, go beyond the
degeneracy you are looking to compute for best results
"""
import pandas as pd
import matplotlib.pyplot as plt

# Set range to
upper = 30

# dimensions
n = range(1, upper)
m = range(1, upper)
l = range(1, upper)
e = []


# remove duplicate values
def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# iterate over all values
for n_ in n:
    for m_ in m:
        for l_ in l:
            a = n_**2 + m_**2 + l_**2
            e.extend([a])

# list processing
e = sorted(e)
consec = remove(e)

# dictionary of {energy level: (energy, degeneracy)}
index = 1
values = {}
degeneracy = []
for val in consec:
    d = e.count(val)
    values.update({index: (val, d)})
    degeneracy.append(d)
    index += 1

print(values)

hist_val = pd.Series(degeneracy)

title = 'Degeneracy Histogram: Range from 1-' + str(upper-1)
hist_val.plot.hist(bins=70, rwidth=0.9, color='#607c8e')
plt.title(title)
plt.xlabel('Degeneracy')
plt.ylabel('Frequency')
plt.show()
