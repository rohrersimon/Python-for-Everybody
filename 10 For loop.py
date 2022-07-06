largest_so_far = None
for i in [1, 6, 9, 256, 3]:
    if largest_so_far is None:
        largest_so_far = i
    print(i)
    if i > largest_so_far:
        largest_so_far = i
print ('Largest =', largest_so_far)