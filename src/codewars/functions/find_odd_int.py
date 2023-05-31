def find_odd_int(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i
