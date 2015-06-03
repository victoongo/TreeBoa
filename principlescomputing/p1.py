"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line2 = list(line)
    ind = 0
    while ind < len(line):
        if line[ind] == 0:
            line2.remove(0)
        ind += 1
    size = len(line2)
    ind = 0
    line_out = []
    while ind < size & size > 0:
        if ind == size - 1:
            line_out.append(line2[ind])
            ind += 1
        elif line2[ind] == line2[ind + 1]:
            line_out.append(line2[ind] * 2)
            ind += 2
        else:
            line_out.append(line2[ind])
            ind += 1
    diff = len(line) - len(line_out)
    for ind in range(diff):      
        line_out.append(0)
    return line_out


t = [4,2,2]
print t, merge(t)
t = [8, 4]
print t, merge(t)
t = [2,2,2,2]
print t, merge(t)
t = [2,0,2,2]
print t, merge(t)
t = [2,0,2,4]
print t, merge(t)
