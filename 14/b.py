
v = [64, 65, 63, 68, 69, 69, 64]

x = 44098
p = 0

p += 1000000000 - x - 1
p = p % len(v)

print(v[p])


x = 6645
v = [int(y) for y in "104733 104715 104698 104692 104707 104742 104758 104788 104815 104842 104883 104903 104931 104958 104958 104961 104945 104913 104897 104844 104805 104758".split()]
print(v)

p += 1000000000 - x - 1
p = p % len(v)

print(v[p])


