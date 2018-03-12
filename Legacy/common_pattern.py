from suffix_trees import STree

sequences = ['0-++++-++--0--+++---++0-++-0-++-++--++--+--+++---',
             '++-+0+---++--+0--+00-++-+-+0----+0-+-+-++--+0--',
             '+---++--+0--+00-++-+-+0----+0-+-+-++--',
             '-------------------------------------']

sequences = sorted(sequences, key=len)

suffix_tree = STree.STree(sequences)
matches = []
window_size = len(suffix_tree.lcs())
window_lower = 0
window_upper = window_lower + window_size

if window_size == 0:
    print('No Match')

else:
    matches.append(suffix_tree.lcs())

while window_size != 0:
    sequences_copy = sequences[:]
    sequences_copy[0] = sequences[0][window_lower:window_upper]
    suffix_tree = STree.STree(sequences_copy)
    if not suffix_tree.lcs() in matches and suffix_tree.lcs() != "":
        matches.append(suffix_tree.lcs())
    window_lower += 1
    window_upper += 1
    if window_upper == len(sequences[0]) - 1:
        window_size -= 1
        window_lower = 0
        window_upper = window_lower + window_size
print(matches)
